import logging  # Added for logging

from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import json
from jsonschema import validate

from flask_app import app

# Added for logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Connecting to the ElasticSearch instance
es = Elasticsearch(
    app.config['ELASTICSEARCH_HOST'],
    api_key=app.config['ELASTICSEARCH_API_KEY'],
    request_timeout=30,
)

# Load the SentenceTransformer model
model = SentenceTransformer('all-mpnet-base-v2')

def handleUserQuestion(question):
    # Generate embedding for the query
    query_embedding = model.encode(question, convert_to_tensor=True)
    query_embedding = query_embedding.cpu().detach().numpy().flatten()

    # Search ElasticSearch for relevant passages
    search_body = {
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.queryVector, 'Embedding') + 1.0",
                    "params": {"queryVector": query_embedding}
                }
            }
        }
    }
    response = es.search(index="search-qa_system_index", body=search_body, size=3)

    # Extract relevant passages and metadata
    relevant_passages = []
    for hit in response['hits']['hits']:
        passage = hit['_source']['Passage']
        metadata = hit['_source']['Metadata']
        relevance_score = hit['_score']
        relevant_passages.append({"passage": passage, "metadata": metadata, "relevance_score": relevance_score})
    print(relevant_passages)
    return relevant_passages

def handleUploadDocument(passage, metadata):
    print("Uploading document")
    # Generate embedding for the passage
    passage_embedding = model.encode(passage, convert_to_tensor=True)
    passage_embedding = passage_embedding.cpu().detach().numpy().flatten()

    # Index the data
    document = {
        "Passage": passage,
        "Metadata": json.dumps(metadata, indent=4),
        "Embedding": passage_embedding
    }
    es.index(index="search-qa_system_index", body=document)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        data = request.json

        # Added request/response validation
        request_schema = {
            "type": "object",
            "properties": {
                "question": {"type": "string"}
            },
            "required": ["question"]
        }
        validate(data, request_schema)

        user_question = data.get('question')

        # Added logging
        logging.info(f"Received question: {user_question}")

        # handling the retrieval of the passage based on the question
        relevant_passages = handleUserQuestion(user_question)

        return jsonify({"answers": relevant_passages}), 200

    except Exception as e:
        # Added logging of errors
        logging.error(f"Error in ask_question: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/upload_document', methods=['POST'])
def upload_document():
    try:
        data = request.json
        passage = data.get('passage')
        metadata = data.get('metadata')

        # Added request/response validation
        request_schema = {
            "type": "object",
            "properties": {
                "passage": {"type": "string"},
                "metadata": {"type": "object"}
            },
            "required": ["passage", "metadata"]
        }
        validate(data, request_schema)

        # Added logging
        logging.info(f"Received document: {data}")

        # handling the upload of the document
        handleUploadDocument(passage, metadata)

        return jsonify({"message": "Document uploaded successfully"}), 200

    except Exception as e:
        # Added logging of errors
        logging.error(f"Error in upload_document: {str(e)}")
        return jsonify({"error": str(e)}), 500

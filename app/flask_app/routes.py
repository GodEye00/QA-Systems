from flask import request, jsonify
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import numpy as np

from flask_app import app

# Connecting to the ElasticSearch instance
es = Elasticsearch(
  "https://2231c2d310594075954cdcba0566089b.us-central1.gcp.cloud.es.io:443",
  api_key="YkczVjI0b0I3eU96R3ZfYWFmUE86VGkzRzJiakhSXy1LSW5aWjd5Z0RKZw==",
  request_timeout=30,
)

# Load the SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        data = request.json
        user_question = data.get('question')

        # Generate embedding for the query
        query_embedding = model.encode(user_question, convert_to_tensor=True)
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
        response = es.search(index="passage_index", body=search_body, size=3)

        # Extract relevant passages and metadata
        relevant_passages = []
        for hit in response['hits']['hits']:
            passage = hit['_source']['Passage']
            metadata = hit['_source']['Metadata']
            relevance_score = hit['_score']
            relevant_passages.append({"passage": passage, "metadata": metadata, "relevance_score": relevance_score})

        return jsonify({"answers": relevant_passages}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload_document', methods=['POST'])
def upload_document():
    try:
        data = request.json
        passage = data.get('passage')
        metadata = data.get('metadata')

        # Generate embedding for the passage
        passage_embedding = model.encode(passage, convert_to_tensor=True)
        passage_embedding = passage_embedding.cpu().detach().numpy().flatten()

        # Index the data
        document = {
            "Passage": passage,
            "Metadata": metadata,
            "Embedding": passage_embedding
        }
        es.index(index="passage_index", body=document)

        return jsonify({"message": "Document uploaded successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

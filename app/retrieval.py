from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch 
import pandas as pd
import numpy as np
import ast

# connecting to elasticsearch
es = Elasticsearch(
  "https://2231c2d310594075954cdcba0566089b.us-central1.gcp.cloud.es.io:443",
  api_key="YkczVjI0b0I3eU96R3ZfYWFmUE86VGkzRzJiakhSXy1LSW5aWjd5Z0RKZw==",
  timeout=30,
)

# Load the SentenceTransformer model 
model = SentenceTransformer('all-mpnet-base-v2')

# Load the user queries 
user_queries = [
    "What are the legal implications of copyright infringement?",
    "How is liability determined in a personal injury case?",
]

def retrievePassages(user_queries):
    print("About to retrieve passages for queries", user_queries)
    # initializing an empty list which will be used to store the results of the search
    results = []

    # Defining the index
    index = "search-qa_system_index"

    # Defining the number of passages to retrieve
    size = 3

    # Processing each query
    for query in user_queries:
        # Generating the embeddings for every query in the user_queries
        query_embedding = model.encode(query, convert_to_tensor=True)
        query_embedding = query_embedding.cpu().detach().numpy().flatten()
            
        # Searching elasticsearch for the matched passages
        body = {
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
        response = es.search(index=index, body=body)
        
        # Getting the needed passages and metadata from the search response
        needed_passages = []
        for hit in response['hits']['hits']:
            passage = hit['_source']['Passage']
            metadata = hit['_source']['Metadata']
            score = hit['_score']
            needed_passages.append((passage, metadata, score))
            
        # sorting the needed passages by their score
        needed_passages.sort(key=lambda x: x[2], reverse=True)
        
        # extracting the top 3 passages
        top_passages = needed_passages[:size]
        
        print("Passages are: ",needed_passages)
        
        # extracting the necessary information for csv output
        passage_texts, metadata, score = zip(*top_passages)
        passage_texts = list(passage_texts)
        metadata = list(metadata)
        score = list(score)
        
        results.append({
            "Question": query,
            "Passage 1": passage_texts[0],
            "Relevance Score 1": score[0],
            "Passage 1 Metadata": metadata[0],
            "Passage 2": passage_texts[1],
            "Relevance Score 2": score[1],
            "Passage 2 Metadata": metadata[1],
            "Passage 3": passage_texts[2],
            "Relevance Score 3": score[2],
            "Passage 3 Metadata": metadata[2]
        })
        
    # Creating a DataFrame from the results
    results_df = pd.DataFrame(results)

    # saving final results to the questions_answers.csv
    results_df.to_csv('../docs/question_answers.csv', index=False)
    
    



def main():
    print("This is the main function in my_function.py")

if __name__ == "__main__":
    main()











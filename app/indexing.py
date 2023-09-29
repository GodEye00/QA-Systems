from elasticsearch import Elasticsearch, helpers
import pandas as pd
import ast


# Connecting to elasticsearch
es = Elasticsearch(
  "https://2231c2d310594075954cdcba0566089b.us-central1.gcp.cloud.es.io:443",
  api_key="YkczVjI0b0I3eU96R3ZfYWFmUE86VGkzRzJiakhSXy1LSW5aWjd5Z0RKZw==",
  request_timeout=30,
)

# Defining the index for the mapping
mapping = {
    "mappings": {
        "properties": {
            "Passage": {"type": "text"},
            "Metadata": {"type": "text"},
            "Embedding": {
                            "type": "dense_vector",
                            "dims": 768,
                            "index": True,
                            "similarity": "cosine"
                        }
        }
    }
}

# creating the index for the search
es_index = "search-qa_system_index"
es.indices.delete(index=es_index)
es.indices.create(index=es_index, body=mapping)

# Loading the passage_metadata_emb.csv file
df = pd.read_csv('../docs/passage_metadata_emb.csv')


# Preparing the passage_metadata for indexing purposes
indexing_data = []
for index, row in df.iterrows():
    document = {
        "Passage": row['Passage'],
        "Metadata": row['Metadata'],
        "Embedding": ast.literal_eval(row['Embedding']),
    }
    indexing_data.append({
        "_index": es_index, "_source": document
    })
    # es.index(index=es_index, body=document)

# Finally indexing the data
helpers.bulk(es, indexing_data)


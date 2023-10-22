from elasticsearch import Elasticsearch, helpers
import pandas as pd
import ast
import os


# Connecting to elasticsearch
es = Elasticsearch(
    cloud_id=os.environ.get('ELASTICSEARCH_CLOUD_ID'),
    api_key=os.environ.get('ELASTICSEARCH_API_KEY'),
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
es_index = os.environ.get('ELASTICSEARCH_INDEX')
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


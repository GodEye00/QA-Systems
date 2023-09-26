from elasticsearch import Elasticsearch, helpers
import pandas as pd

# Connecting to elasticsearch
es = Elasticsearch(
  "https://2231c2d310594075954cdcba0566089b.us-central1.gcp.cloud.es.io:443",
  api_key="VTBvSzBvb0J5MXhjdGpHeVJDWUU6eXVsazVuSGlSaE9qOFNHTEZmb2dNdw=="
)

# Defining the index for the mapping
mapping = {
    "mappings": {
        "properties": {
            "Passage": {"type": "text"},
            "Metadata": {"type": "text"},
            "Embedding": {"type": "dense_vector", "dims":768}
        }
    }
}

# creating the index for the search
# index = "passage_index"
# es.indices.create(index, body=mapping)

# Loading the passage_metadata_emb.csv file
df = pd.read_csv('../docs/passage_metadata_emb.csv')

# Preparing the passage_metadata for indexing purposes
indexing_data = []
for index, row in df.iterrows():
    document = {
        "Passage": row['Passage'],
        "Metadata": row['Metadata'],
        "Embeddings": row['Embedding'],
    }
    indexing_data.append({
        "_index": index, "_source": document
    })
    
    
# Finally indexing the data
helpers.bulk(es, indexing_data)


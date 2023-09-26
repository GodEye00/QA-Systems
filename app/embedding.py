from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd


# Loading sentence transformers model called 'all-mpnet-base-v2'
model = SentenceTransformer('all-mpnet-base-v2')

# Loading the passage_metadata.csv file
passage_metadata_df = pd.read_csv('../docs/passage_metadata.csv')

# initializing an empty list to store passage metadata and embeddings 
passage_metadata_emb_trio = []

# Generating embeddings for every passage in the passage_metadata
for index, row in passage_metadata_df.iterrows():
    passage = row['Passage']
    metadata = row['Metadata']
    
    # Generating embeddings for every passage
    passage_embedding = model.encode(passage, convert_to_tensor=True)
    
    # Converting the embedding tensor to a numpy array 
    passage_embedding = passage_embedding.cpu().detach().numpy().flatten()
    
    # Appending the embedding to the list 
    passage_metadata_emb_trio.append({
        'Passage': passage,
        'Metadata': metadata,
        'Embedding': passage_embedding,
    })
    
    
# Creating a DataFrame from the trio 
passage_metadata_emb_df = pd.DataFrame(passage_metadata_emb_trio)

# Writing the results to passage_metadata_emb.csv 
passage_metadata_emb_df.to_csv('../docs/passage_metadata_emb.csv', index=False) 





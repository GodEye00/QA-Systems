'''
A helper for writing and reading items from file
'''

import os 
import json 
import csv 

# Specifying the file path to write and retrieve data to and fro respectively
corpus = "../Corpus"
output_csv_path = "../docs/passage_metadata.csv"

# Creating an list that will store all retrieved passages and their metadata pairs
passage_metadata_pairs = []

# Going through every file in the corpus folder 
for filename in os.listdir(corpus):
    if filename.endswith("_Technical.txt"):
        technical_path = os.path.join(corpus, filename)
        metadata_path = os.path.join(corpus, filename.replace("_Technical.txt", "_Metadata.json"))
        
        # Reading the metadata
        with open(metadata_path, 'r') as metadata_file:
            metadata = json.load(metadata_file)
        
        # And then reading the technical details 
        with open(technical_path, 'r') as technical_file:
            technical = technical_file.read()
            
            # splitting into paragraphs
            paragraphs = technical.split('__paragraph__')
            
            # combining paragraphs together and spitting into 5 sentence chunks
            chunk_size = 5
            for i in range(0, len(paragraphs), chunk_size):
                chunk = " ".join(paragraphs[i:i+chunk_size])
                passage_metadata_pairs.append({"Passage": chunk, "Metadata": metadata})
                
with open(output_csv_path, 'a', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Passage', 'Metadata']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    for pair in passage_metadata_pairs:
        writer.writerow(pair)
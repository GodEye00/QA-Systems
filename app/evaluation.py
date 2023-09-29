import pandas as pd
import numpy as np

from retrieval import retrievePassages

# Load user queries
user_queries = open('../user_queries.txt', 'r').readlines()
user_queries = [query.strip() for query in user_queries]

# retrievePassages(user_queries)

# Load the retrieved passages (from questions_answers.csv)
retrieved_passages = pd.read_csv('../docs/question_answers.csv')

# Initialize an empty list to store evaluation data
evaluation_data = []

# Loop through each user query
for query in user_queries:
    # Extract relevant information for the query
    relevant_info = retrieved_passages[retrieved_passages['Question'] == query].iloc[0]
    
    # Append to evaluation data
    evaluation_data.append({
        "Question": query,
        "Passage 1": relevant_info['Passage 1'],
        "Relevance Score 1": relevant_info['Relevance Score 1'],
        "Passage 1 Metadata": relevant_info['Passage 1 Metadata'],
        "Is Passage 1 Relevant? (Yes/No)": None,  # Placeholder for manual rating
        "Passage 2": relevant_info['Passage 2'],
        "Relevance Score 2": relevant_info['Relevance Score 2'],
        "Passage 2 Metadata": relevant_info['Passage 2 Metadata'],
        "Is Passage 2 Relevant? (Yes/No)": None,  # Placeholder for manual rating
        "Passage 3": relevant_info['Passage 3'],
        "Relevance Score 3": relevant_info['Relevance Score 3'],
        "Passage 3 Metadata": relevant_info['Passage 3 Metadata'],
        "Is Passage 3 Relevant? (Yes/No)": None  # Placeholder for manual rating
    })

# Create a DataFrame from the evaluation data
evaluation_df = pd.DataFrame(evaluation_data)

# Save to evaluation.csv
evaluation_df.to_csv('../docs/evaluation.csv', index=False)

import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'  # Replace with your own API key

# Load the retrieved passages
retrieved_passages = pd.read_csv('docs/questions_answers.csv')

# Define a function to generate a direct answer using GPT-3
def generate_direct_answer(question, passage):
    prompt = f"Question: {question}\nAnswer:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=['\n']
    )

    answer = response.choices[0].text.strip()
    return answer

# Initialize an empty list to store the data
questions_answers_gen = []

# Loop through each retrieved passage
for _, row in retrieved_passages.iterrows():
    question = row['Question']
    passages = [row[f'Passage {i}'] for i in range(1, 4)]
    metadata = [row[f'Relevance Score {i}'] for i in range(1, 4)]

    # Generate direct answers for each passage
    direct_answers = [generate_direct_answer(question, passage) for passage in passages]

    # Append the data to the list
    questions_answers_gen.append({
        "Question": question,
        "Passage 1": passages[0],
        "Relevance Score 1": metadata[0],
        "Passage 1 Metadata": row['Passage 1 Metadata'],
        "Passage 2": passages[1],
        "Relevance Score 2": metadata[1],
        "Passage 2 Metadata": row['Passage 2 Metadata'],
        "Passage 3": passages[2],
        "Relevance Score 3": metadata[2],
        "Passage 3 Metadata": row['Passage 3 Metadata'],
        "Generative AI Answer": direct_answers
    })

# Create a DataFrame from the data
questions_answers_gen_df = pd.DataFrame(questions_answers_gen)

# Save to questions_answers_gen.csv
questions_answers_gen_df.to_csv('docs/questions_answers_gen.csv', index=False)

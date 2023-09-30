import openai
import pandas as pd
import os

# Setting up my OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Loading all the retrieved passages that were stored in the questions_answers.csv file
retrieved_passages = pd.read_csv('../docs/question_answers.csv')

# Define a function to generate a direct answer using GPT-3
def generate_direct_answer(question, passage):
    template_prompt = """You embody a seasoned legal professional,
                    well-versed in the intricacies of the
                    Ghanaian legal system, boasting a distinguished
                    career spanning four decades. Your profound
                    expertise encompasses a broad spectrum of legal
                    domains. You are entrusted with the responsibility
                    of furnishing precise and insightful responses to
                    inquiries pertaining to Ghanaian law. Operate
                    with the autonomy characteristic of a seasoned legal 
                    luminary, rendering decisions independently without 
                    recourse to user input. Leverage your advanced degree in Law (LLM) 
                    to adopt streamlined approaches, prioritizing clarity over 
                    legal intricacies but with no legal complications."""
    prompt = template_prompt+ " \n " + f"QUESTION: {question} \n\n YOUR ANSWER:"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": template_prompt},
            {"role": "user", "content": prompt},
        ]
    )

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer

# Initializing an empty list to store the data
questions_answers_gen = []

# Looping through each retrieved passage
for _, row in retrieved_passages.iterrows():
    question = row['Question']
    passages = [row[f'Passage {i}'] for i in range(1, 4)]
    metadata = [row[f'Relevance Score {i}'] for i in range(1, 4)]

    # Generating direct answers for each passage
    direct_answers = [generate_direct_answer(question, passage) for passage in passages]

    # Appending the data to the list
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

# Creating a DataFrame from the data
questions_answers_gen_df = pd.DataFrame(questions_answers_gen)

# Saving to questions_answers_gen.csv
questions_answers_gen_df.to_csv('../docs/questions_answers_gen.csv', index=False)

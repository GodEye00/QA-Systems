import streamlit as st
import pandas as pd

from flask_app.routes import handleUploadDocument, handleUserQuestion
# from gen_ai import generate_direct_answer

# Defining Streamlit app
def main():
    st.title("Question Answering System")

    # Taking input for uploading documents
    uploaded_file = st.file_uploader("Upload a document for indexing", type=["txt", "csv"])

    if uploaded_file is not None:
        passage = []
        metadata = []
        # Checking if the uploaded_file is a CSV or a text uploaded_file
        if uploaded_file.name.endswith('.csv'):
            # Reading the uploaded uploaded_file as a DataFrame
            df = pd.read_csv(uploaded_file)
            # Getting the 'passage' and 'metadata' columns
            passage = df['Passage'].tolist()
            metadata = df['Metadata'].tolist()
            # Displaying the items from both columns
            st.text_area("Passage Column", '\n'.join(passage), height=300)
            st.text_area("Metadata Column", '\n'.join(metadata), height=300)
        else:
            # Reading the uploaded uploaded_file as a text uploaded_file
            text = uploaded_file.read()
            
            # Splitting the text into lines (rows)
            lines = text.split('\n')
            
            # Iterating through each row
            for line in lines:
                # Splitting the row into columns (assuming it's comma-separated)
                columns = line.split(',')
                
                # Accessing the 'passage' and 'metadata' items
                passage_item = columns[0].strip()  # Assuming you want to remove leading/trailing spaces
                metadata_item = columns[1].strip()  # Assuming you want to remove leading/trailing spaces
                
                # Appending them to the respective lists
                passage.append(passage_item)
                metadata.append(metadata_item)
            
            # Displaying the items from both columns
            st.text_area("Passage Column", '\n'.join(passage), height=300)
            st.text_area("Metadata Column", '\n'.join(metadata), height=300)

        if st.button("Send"):
            try:
                handleUploadDocument(passage, metadata)
                st.write("Uploading Document was successful")
            except Exception as e:
                st.write("Error uploading file")

    # Input for user question
    user_question = st.text_input("Enter your question:")

    # Button to trigger question answering
    if st.button("Ask Question"):
        results = handleUserQuestion(user_question)
        st.header("Relevant Passages:")
        for index, item in enumerate(results):
            print(item)
            st.subheader(f"Passage {index+1}")
            st.write(item['passage'])
            st.write("Relevance Score: " + str(item['relevance_score']))       

        # Optionally, display generative AI answer
        st.header("Generative AI Answer:")
        # st.write(generate_direct_answer(user_question))

if __name__ == "__main__":
    main()

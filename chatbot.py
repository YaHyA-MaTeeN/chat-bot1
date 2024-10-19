import streamlit as st
from transformers import pipeline
import random

# Initialize the Hugging Face pipeline for question answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# List of general apology messages
apologies = [
    "YAHYA here, I know I messed up before! I'm really sorry about that. Now, let me help with your question.",
    "I'm still trying to make up for that mistake I made earlier... Forgive me! Let's see how I can help you now.",
    "YAHYA sincerely apologizes for what happened earlier. Hopefully, I can make things right with this answer.",
    "I hope you can forgive me for my previous mistake. YAHYA is ready to assist you with your query!",
    "I realize I wasn't great earlier. My apologies, YAHYA here. Let me make it up to you by answering your question."
]

# Function to generate a random apology
def get_random_apology():
    return random.choice(apologies)

# Define chatbot function
def chat_with_yahya(question):
    if question:
        # Get a random apology
        apology_message = get_random_apology()

        # Using the question-answering model
        context = "This is a chatbot that tries to answer any general question based on a large dataset."
        result = qa_pipeline(question=question, context=context)

        # Extract the answer
        answer = result['answer']

        # Return the full response with the apology message
        return f"{apology_message}\n\nAnswer: {answer}"
    return "Please ask me a question."

# Streamlit app setup
def main():
    st.title("YAHYA's Apologetic Chatbot 🤖")

    # Input for user's question
    user_question = st.text_input("Ask me anything:")

    # If the user submits a question, get the chatbot response
    if st.button("Get Answer"):
        response = chat_with_yahya(user_question)
        st.write(response)

# Run the app
if __name__ == "__main__":
    main()

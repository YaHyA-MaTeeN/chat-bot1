import streamlit as st
from transformers import pipeline
import random


# Initialize the Hugging Face pipeline for question answering using PyTorch
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", framework="pt")

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

        # Here, you can set a more relevant context based on the question or general knowledge
        context = "This chatbot uses advanced models to answer questions across various domains. You can ask about technology, science, or general knowledge."

        # Using the question-answering model
        try:
            result = qa_pipeline(question=question, context=context)

            # Check if an answer is found
            if result['score'] < 0.1:  # Adjust this threshold based on experimentation
                answer = "I couldn't find a suitable answer for that. Please try asking something else!"
            else:
                answer = result['answer']

            # Return the full response with the apology message
            return f"{apology_message}\n\nAnswer: {answer}"
        except Exception as e:
            return f"{apology_message}\n\nAn error occurred: {str(e)}"
    
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

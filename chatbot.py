import streamlit as st
from transformers import pipeline
import random

# Initialize the Hugging Face pipeline for question answering using Flan-T5
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large", framework="pt")

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

# Function to define chatbot responses
def chat_with_yahya(question):
    if question:
        # Get a random apology
        apology_message = get_random_apology()

        # Create a dynamic context (this can be more advanced in real use)
        context = "You can ask me about various topics, including science, technology, history, and general knowledge. I will do my best to provide an accurate answer based on the information I have."

        # Using the text-generation model from Flan-T5
        try:
            # Generate an answer using Flan-T5
            result = qa_pipeline(f"Answer the question: {question}")

            # Extracting the result (Flan-T5 provides an array, so we pick the first result)
            answer = result[0]['generated_text']

            # Return the full response with the apology message
            return f"{apology_message}\n\nAnswer: {answer}"
        except Exception as e:
            return f"{apology_message}\n\nAn error occurred: {str(e)}"

    return "Please ask me a question."


# Streamlit app setup
def main():
    # Set up cute pastel theme colors with CSS
    st.markdown("""
        <style>
        body {
            background-color: #FFF7F0;
        }
        .stApp {
            background-color: #FDE4E4;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stButton {
            background-color: #FCE8E8;
            border: 1px solid #F9C6C6;
            border-radius: 12px;
            padding: 10px;
            margin: 10px 0;
        }
        .stButton {
            background-color: #FFDFDF;
        }
        h1 {
            color: #FF69B4;
            font-family: "Comic Sans MS", "Comic Sans", cursive;
            text-align: center;
        }
        .chat-response {
            background-color: #FFE4E1;
            border: 2px solid #FADADD;
            border-radius: 12px;
            padding: 15px;
            font-family: "Comic Sans MS", cursive;
            font-size: 16px;
            color: #6B5B95;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("YAHYA's Apologetic Chatbot 🤖")

    # Display cute image (you can add any image URL you want)
    st.image("https://imgur.com/a/BoJ508n", use_column_width=True)

    # Input for user's question
    user_question = st.text_input("Ask me anything:")

    # If the user submits a question, get the chatbot response
    if st.button("Get Answer"):
        response = chat_with_yahya(user_question)
        st.markdown(f"<div class='chat-response'>{response}</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()

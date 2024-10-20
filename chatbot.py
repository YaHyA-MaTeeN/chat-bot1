import streamlit as st
from transformers import pipeline
import random

# Initialize the Hugging Face pipeline for question answering using Flan-T5
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large", framework="pt")

# List of general apology messages
apologies = [
    "YAHYA here, I know I messed up before! 😞 I'm really sorry about that. Now, let me help with your question.",
    "I'm still trying to make up for that mistake I made earlier... Forgive me! 🥺 Let's see how I can help you now.",
    "YAHYA sincerely apologizes for what happened earlier. 🙏 Hopefully, I can make things right with this answer.",
    "I hope you can forgive me for my previous mistake. 🥺 YAHYA is ready to assist you with your query!",
    "I realize I wasn't great earlier. 😔 My apologies, YAHYA here. Let me make it up to you by answering your question."
]

# Function to generate a random apology
def get_random_apology():
    return random.choice(apologies)

# Function to define chatbot responses
def chat_with_yahya(question):
    if question:
        # Get a random apology
        apology_message = get_random_apology()

        # Create a dynamic context (you can enhance this)
        context = "You can ask me about various topics, including science, technology, history, and general knowledge. I will do my best to provide an accurate answer based on the information I have."

        # Using the text-generation model from Flan-T5
        try:
            # Generate an answer using Flan-T5
            result = qa_pipeline(f"Answer the question: {question}")

            # Extracting the result
            answer = result[0]['generated_text']

            # Return the full response with the apology message
            return f"{apology_message}\n\n**Answer:** {answer}"
        except Exception as e:
            return f"{apology_message}\n\nAn error occurred: {str(e)}"

    return "Please ask me a question."

# Streamlit app setup
def main():
    # App title and styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f0f5;
        }
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1527181152855-fc03fc7949c8");
            background-size: cover;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.title("🤖 YAHYA's Apologetic Chatbot 💬")

    # Input for user's question
    user_question = st.text_input("Ask me anything:", placeholder="Type your question here...")

    # If the user submits a question, get the chatbot response
    if st.button("Get Answer"):
        with st.spinner('YAHYA is thinking... 💭'):
            response = chat_with_yahya(user_question)
        # Display chatbot response
        st.write(response)

    # Apology section (add cuteness here)
    st.markdown(
        """
        <div style='text-align: center; color: gray;'>
        <p style='font-size: 0.85em;'>I hope I got it right this time! 💖</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()

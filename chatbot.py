{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPZ+jHxf8nKyv8ZWLyFVRGj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/YaHyA-MaTeeN/chat-bot1/blob/main/chatbotidknooo.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uUwmv7fepS6o"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from transformers import pipeline\n",
        "import random\n",
        "\n",
        "# Initialize the Hugging Face pipeline for question answering\n",
        "qa_pipeline = pipeline(\"question-answering\", model=\"deepset/roberta-base-squad2\")\n",
        "\n",
        "# List of general apology messages\n",
        "apologies = [\n",
        "    \"YAHYA here, I know I messed up before! I'm really sorry about that. Now, let me help with your question.\",\n",
        "    \"I'm still trying to make up for that mistake I made earlier... Forgive me! Let's see how I can help you now.\",\n",
        "    \"YAHYA sincerely apologizes for what happened earlier. Hopefully, I can make things right with this answer.\",\n",
        "    \"I hope you can forgive me for my previous mistake. YAHYA is ready to assist you with your query!\",\n",
        "    \"I realize I wasn't great earlier. My apologies, YAHYA here. Let me make it up to you by answering your question.\"\n",
        "]\n",
        "\n",
        "# Function to generate a random apology\n",
        "def get_random_apology():\n",
        "    return random.choice(apologies)\n",
        "\n",
        "# Define chatbot function\n",
        "def chat_with_yahya(question):\n",
        "    if question:\n",
        "        # Get a random apology\n",
        "        apology_message = get_random_apology()\n",
        "\n",
        "        # Using the question-answering model\n",
        "        context = \"This is a chatbot that tries to answer any general question based on a large dataset.\"\n",
        "        result = qa_pipeline(question=question, context=context)\n",
        "\n",
        "        # Extract the answer\n",
        "        answer = result['answer']\n",
        "\n",
        "        # Return the full response with the apology message\n",
        "        return f\"{apology_message}\\n\\nAnswer: {answer}\"\n",
        "    return \"Please ask me a question.\"\n",
        "\n",
        "# Streamlit app setup\n",
        "def main():\n",
        "    st.title(\"YAHYA's Apologetic Chatbot 🤖\")\n",
        "\n",
        "    # Input for user's question\n",
        "    user_question = st.text_input(\"Ask me anything:\")\n",
        "\n",
        "    # If the user submits a question, get the chatbot response\n",
        "    if st.button(\"Get Answer\"):\n",
        "        response = chat_with_yahya(user_question)\n",
        "        st.write(response)\n",
        "\n",
        "# Run the app\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "id": "OHH0dZN7qD14"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}

import os
from dotenv import load_dotenv
from groq import Groq

import streamlit as st

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("groq_api_key")


#choose the model you want to use and define a function to call the API
def groq_api(api_key, userinput):
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": userinput
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    full_response = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            full_response += content
    return full_response


# Streamlit UI
st.title("Chatbot using Groq API")
st.write("Type your question below:")

user_input = st.text_input("Ask your question:")

if user_input:
    with st.spinner("Processing..."):
        response = groq_api(api_key, user_input)
        st.write(response)
        st.success("Thank you for using the Groq API chatbot!")

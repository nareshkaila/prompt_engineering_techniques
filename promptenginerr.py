import streamlit as st
import google.generativeai as genai
import os

# Set your Gemini API key (store securely using environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the Gemini model
model = genai.GenerativeModel("gemini-pro")

def retriever_info(query):
    # Dummy implementation for example purposes
    return "about prime minister of India"

def rag_query(query):
    retrieved_info = retriever_info(query)
    augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"

    try:
        response = model.generate_content(augmented_prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# Streamlit UI
st.title("🔍 Gemini RAG Prompt Query Interface")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        response = rag_query(user_input)
        st.write("Response:", response)
    else:
        st.warning("Please enter a query.")

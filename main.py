import streamlit as st
from transformers import pipeline
import torch

# Create a Streamlit app title and description
st.title("Hugging Face Transformers App")
st.write("Simple app for NLP tasks using Hugging Face Transformers.")

# Create a dropdown to select the NLP task
nlp_task = st.selectbox("Select an NLP task", ("Text Generation", "Sentiment Analysis", "Text Summerization"))

# Load the appropriate Hugging Face pipeline based on the selected task
if nlp_task == "Text Generation":
    generator = pipeline("text-generation")
elif nlp_task == "Sentiment Analysis":
    sentiment_classifier = pipeline("sentiment-analysis")
elif nlp_task == "Text Summerization":
    summarizer = pipeline("summarization")

# Create an input text box for user input
user_input = st.text_input("Enter your text")

# Process the user input based on the selected NLP task
if nlp_task == "Text Generation":
    if user_input:
        generated_text = generator(user_input, max_length=50, num_return_sequences=1)
        st.write("Generated Text:")
        st.write(generated_text[0]["generated_text"])
elif nlp_task == "Sentiment Analysis":
    if user_input:
        sentiment_result = sentiment_classifier(user_input)
        st.write("Sentiment Analysis:")
        st.write(sentiment_result[0])
elif nlp_task == "Text Classification":
    if user_input:
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        st.write("Text Classification:")
        st.write(summary[0]['summary_text'])

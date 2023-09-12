import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
st.title("Fysiinc Summarizer")
input_data = st.text_area("Enter the paragraph")

if st.button("Generate"):
    if input_data:
        output = query({
            'inputs': input_data
        })
        st.write("Your Summary is ready!!!")
        st.write(output[0]['summary_text'])
    
    else:
        st.warning("Please Enter something")



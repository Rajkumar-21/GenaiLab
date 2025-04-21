import requests
import streamlit as st

def get_groq_response(input_text):
    response = requests.post(
        "http://localhost:8000/groq_prompt/invoke",
        json={'input':{'topic': input_text}})
    
    return response.json()['output']['content']


st.title("Groq Prompt API Client")
st.write("This is a simple Streamlit app to interact with the Groq LLM API.")
input_text = st.text_input("Enter your prompt:")
    
if st.button("Submit"):
    if input_text:
        with st.spinner("Generating response..."):
            groq_response = get_groq_response(input_text)
            st.success("Response received!")
            st.write(groq_response)
    else:
        st.warning("Please enter a prompt before submitting.")
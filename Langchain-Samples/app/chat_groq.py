from langchain_groq import ChatGroq
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# print("API Key:", os.environ.get("GROQ_API_KEY"))

os.environ["GROQ_API_KEY"]=os.environ.get("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ["LANGCHAIN_SMITH_API_URL"]=LANGSMITH_ENDPOINT
LANGSMITH_PROJECT="Langchain-Examples"
os.environ["LANGCHAIN_PROJECT"]=LANGSMITH_PROJECT
os.environ["LAMGCHAIN_API_KEY"]=os.environ.get("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. you are responding to users to answer questions and provide information."),
        ("human", "Question: {input}"),
    ]
)

st.title("Langchain Groq LLM")
st.write("This is a simple Langchain Groq LLM app.")
input_text = st.text_input("Enter your question:")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
StrOutputParser = StrOutputParser()
chain = prompt | llm | StrOutputParser
if input_text:
    with st.spinner("Generating response..."):
        response = chain.invoke({"input": input_text})
        st.write("Response:")
        st.write(response)
# if __name__ == "__main__":
#     st.run()
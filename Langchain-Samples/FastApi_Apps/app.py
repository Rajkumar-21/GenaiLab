from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

os.environ["GROQ_API_KEY"]=os.environ.get("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ["LANGCHAIN_SMITH_API_URL"]=LANGSMITH_ENDPOINT
LANGSMITH_PROJECT="Langchain-Examples"
os.environ["LANGCHAIN_PROJECT"]=LANGSMITH_PROJECT
os.environ["LAMGCHAIN_API_KEY"]=os.environ.get("LANGCHAIN_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Groq API",
    description="A simple FastAPI app using Langchain Groq",
    version="0.1.0"
)

add_routes(
    app,
    ChatGroq,
    path="/groq",
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

prompt=ChatPromptTemplate.from_template("")
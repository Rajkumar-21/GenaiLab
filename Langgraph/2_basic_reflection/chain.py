from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        "You are a helpful assistant that helps the user to resolve their azure cost optimization and suggesting how can we improve the cost."
        "Generate the best solution for the cost optimisation and suggestion to improve"
        "Also point out the resources and also the cost we save if we follow the suggestions",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]

)


reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        "You are a helpful assistant verify with factual data available on the internet"
        "Always provide practical implementation steps and examples, if applicable.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.environ.get("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm
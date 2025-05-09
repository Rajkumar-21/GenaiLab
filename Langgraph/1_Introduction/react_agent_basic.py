from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain.agents import initialize_agent, tool
from langchain_community.tools import DuckDuckGoSearchResults
import datetime
from langchain_groq import ChatGroq
import httpx
from langchain.llms import huggingface_hub
load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.environ.get("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"]=os.environ.get("GROQ_API_KEY")
search = DuckDuckGoSearchResults(backend="google")
#llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

# # Create a custom httpx client with SSL verification disabled
custom_client = httpx.Client(verify=False)


llm = ChatGroq(
 model="qwen-qwq-32b",
 temperature=0,
 max_tokens=None,
 timeout=None,
 max_retries=2,
)

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("When was Anthropic's MCP Server first last launch and how many days ago was that from this instant")
from langchain import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain_openai import OpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]


search = SerpAPIWrapper()
tools = [Tool.from_function(
    func=search.run,
    name="Search",
    description="useful for when you need to answer questions about current events"
  )]
agent = initialize_agent(tools, llm = OpenAI(), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("When was Avatar 2 released?")
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import YouTubeSearchTool
import langchain_community.tools as tutu
## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

##lets check all the tools in langchain community
print(tutu.__all__)

## kets define the youtube search tool
youtube = YouTubeSearchTool()
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
## define the tools to be used in the agent we are building

tools = [
Tool(
name="youtube",
func=youtube.run,
description="Helps in getting youtube videos",
),

Tool(
name="wiki",
func=wiki.run,
description="Useful to search about a popular entity",
)
]

prefix = "Answer the question asked. You have access to the following tools:"
suffix = "Begin! {chat_history} Question: {input} {agent_scratchpad}"

prompt = ZeroShotAgent.create_prompt(tools,prefix=prefix,suffix=suffix,
input_variables=["input","chat_history","agent_scratchpad"], )

## lets define a variable for memory management in our agent
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain=LLMChain(llm=OpenAI(temperature=0),prompt=prompt)
agent=ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)

agent_chain = AgentExecutor.from_agent_and_tools(
agent=agent, tools=tools, verbose=True, memory=memory )
agent_chain.run(input="Tell me something about SRK. Also, get me the link to one of his movies from YouTube")

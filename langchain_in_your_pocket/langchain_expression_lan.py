import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain.chains import LLMMathChain
from langchain.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate

## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

prompt = ChatPromptTemplate.from_template("What is the city {person} is from? Translate: {sentence} in the city native language")
model = ChatOpenAI()

chain = prompt | model | StrOutputParser
chain.invoke({'person':"Virat kohli",'sentence':"how are you"})

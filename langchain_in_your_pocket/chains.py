import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]
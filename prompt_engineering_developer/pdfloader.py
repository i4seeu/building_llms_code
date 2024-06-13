import os
import openai #import OpenAI
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from langchain.document_loaders import PyPDFLoader


load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


#==== Using OpenAI Chat API =======
llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0.0, model=llm_model) 

### pip install pypdf

loader = PyPDFLoader("../data/react-paper.pdf")
pages = loader.load()

# print(len(pages))

page = pages[0]
# print(pages)
print(page.page_content[0:700]) # first 700 characters on the page
print(page.metadata)
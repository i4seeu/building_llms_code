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

## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

## autosql chain
print("***********auto-SQL Chain*********")
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI()
chain = create_sql_query_chain(llm,db)

response=chain.invoke({"question":"What is the total salary for each department"})

print(response)

## mathchain
print("**************Math chain************")

llm = OpenAI(temperature=0)
llm_math = LLMMathChain.from_llm(llm, verbose=True)
print(llm_math.run("What is the 3rd root of 1498 ?"))

print("************** DALLE model **************")
llm = OpenAI()
# prompt = PromptTemplate.from_template("Generate an image based on the following description: {image_desc}")
prompt = PromptTemplate(
input_variables=["image_desc"],
template="Generate an image based on {image_desc}", )

prompts = ['tennis', 'crying child']

chain = LLMChain(llm=llm, prompt=prompt)
## loop through the description arrays
for x in prompts:
    print(x)
    print(DallEAPIWrapper().run(chain.run(x)))
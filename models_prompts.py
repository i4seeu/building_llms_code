import os
from dotenv import find_dotenv, load_dotenv
import openai
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
#from langchain_community.llms import OpenAI

load_dotenv(find_dotenv()) # load all the environmental variables
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0.7)
print(llm('tell me a joke'))


print("+++++++++++ prompting code +++++++++++++++++++")
## prompting
## from langchain import PromptTemplate
template = """Sentence: {sentence}
Translation in {language}:"""
prompt = PromptTemplate(template=template, input_variables=["sentence", "language"])
print(prompt.format(sentence = "the cat is on the table", language = "spanish"))
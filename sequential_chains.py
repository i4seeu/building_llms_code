from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]

llm = OpenAI()
# This is an LLMChain to write a synopsis given a title of a play.
llm = OpenAI(temperature=0)
template = """You are a comedian. Generate a joke on the following {topic}
Joke:"""
prompt_template = PromptTemplate(input_variables=["topic"], template=template)
joke_chain = LLMChain(llm=llm, prompt=prompt_template)

template = """You are translator. Given a text input, translate it to {language}
Translation:"""
prompt_template = PromptTemplate(input_variables=["language"], template=template)
translator_chain = LLMChain(llm=llm, prompt=prompt_template)

# This is the overall chain where we run these two chains in sequence.

overall_chain = SimpleSequentialChain(chains=[joke_chain, translator_chain], verbose=True)
translated_joke = overall_chain.run("Cats and Dogs")
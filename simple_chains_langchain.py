import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
load_dotenv()
os.environ["OPENAI_API_KEY"]



template = """Sentence: {sentence}
Translation in {language}:"""
prompt = PromptTemplate(template=template, input_variables=["sentence", "language"])


llm = OpenAI(temperature=0)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.predict(sentence="the cat is on the table", language="spanish"))

##  with the new version of langchain the above code can be replaced with the folllowing code

# template2 = """Sentence: {sentence}
# Translation in {language}:"""

# prompt2 = PromptTemplate(template=template, input_variables=["sentence", "language"])

# chain = prompt2 | llm 
# print(chain.arun(sentence="the cat is on the table", language="chichewa"))
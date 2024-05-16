from dotenv import load_dotenv
import os
load_dotenv()
os.environ["OPENAI_API_KEY"]

# Import the string module
import string

# Define the function
def rename_cat(inputs: dict) -> dict:
  # Open the file in read mode
  text = inputs["text"]
  # Create a table that maps punctuation characters to None
  new_text = text.replace('cat', 'Silvester the Cat')
  # Apply the table to the text and return the result
  return {"output_text": new_text}

from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

with open("Cats&Dogs.txt") as f:
    cats_and_dogs = f.read()


transform_chain = TransformChain(
    input_variables=["text"], output_variables=["output_text"], transform=rename_cat
)

template = """Summarize this text:

{output_text}

Summary:"""
prompt = PromptTemplate(input_variables=["output_text"], template=template)

llm_chain = LLMChain(llm=OpenAI(), prompt=prompt)

sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain])

print(sequential_chain.run(cats_and_dogs))
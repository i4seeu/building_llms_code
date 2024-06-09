import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

#==== Using OpenAI Chat API =======
llm_model = "gpt-3.5-turbo"

# chat = ChatOpenAI(temperature=0.9, model=llm_model)
open_ai = OpenAI(temperature=0.7)


template = """ 
 As a children's book writer, please come up with a simple and short (90 words)
 lullaby based on the location
 {location}
 and the main character {name}
 
 STORY:
"""

prompt = PromptTemplate(input_variables=["location", "name"],
                        template=template)

chain_story = LLMChain(llm=open_ai, prompt=prompt, verbose=True)
story = chain_story({"location": "Zanzibar", "name": "Maya"})

print(story['text'])
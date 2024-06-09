import os
from openai import OpenAI
from dotenv import load_dotenv
#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

#==== Using OpenAI Chat API =======
llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0.6, 
                 model=llm_model)

print(llm.predict("My name is Paulo. What is yours?"))
print(llm.predict("Great!  What's my name?")) # we have memory issues!

# How to solve llms memory issues?
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.predict(input="Hello there, I am Paulo")
conversation.predict(input="Why is the sky blue?")
conversation.predict(input="If phenomenon called Rayleigh didn't exist, what color would the sky be?")
conversation.predict(input="What's my name?")


print(f"Memory ===> {memory.buffer} <====")

# print(memory.load_memory_variables({}))
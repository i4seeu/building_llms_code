import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

#LLMS
llm = OpenAI(temperature=0) 
print(llm.invoke("Tell me about stars"))

#ChatModels
messages = [
SystemMessage(content="You're a helpful assistant"),
HumanMessage(content="What should we do to stop pollution?"),]

llm = ChatOpenAI() 
print(llm.invoke(messages))

## prompts
from langchain.prompts.chat import (
ChatPromptTemplate,
SystemMessagePromptTemplate,
AIMessagePromptTemplate,
HumanMessagePromptTemplate,)


template="You are a helpful assistant who can give {category} for given input"
system_message_prompt=SystemMessagePromptTemplate.from_template(template)

human_template="{text}"
human_message_prompt=HumanMessagePromptTemplate.from_template(human_template)

chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chat = ChatOpenAI() 
print(chat(chat_prompt.format_prompt(category="antonyms",text='Rude').to_messages()))
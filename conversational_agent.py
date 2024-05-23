import os
from dotenv import load_dotenv
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

from langchain.schema import (
  AIMessage,
  HumanMessage,
  SystemMessage
)
from langchain.chains import LLMChain, ConversationChain 
from langchain_openai import ChatOpenAI

chat = ChatOpenAI()
messages = [
            SystemMessage(content="You are a helpful assistant that help the user to plan an optimized itinerary."),
            HumanMessage(content="I'm going to Rome for 2 days, what can I visit?")]

output = chat(messages)
print(output.content)

## lets add memory to the conversation bot
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain 

memory = ConversationBufferMemory()
conversation = ConversationChain(
  llm=chat, verbose=True, memory=memory
)

print(conversation.run("Hi there!"))
print(conversation.run("what is the most iconic place in Rome?"))
print(conversation.run("What kind of other events?"))
print(memory.load_memory_variables({}))


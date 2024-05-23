import os
from dotenv import load_dotenv
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain, ConversationChain 
from langchain_openai import ChatOpenAI

chat = ChatOpenAI()


prompt = ChatPromptTemplate.from_messages(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant that help the user to plan an optimized itinerary."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
conversation = LLMChain(
    llm=chat,
    prompt=prompt,
    verbose=False,
    memory=memory
)

while True:
    query = input('you: ')
    if query == 'q':
        break
    output = conversation({"question": query})
    print('User: ', query)
    print('AI system: ', output['text'])
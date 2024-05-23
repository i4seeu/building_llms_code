from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

import os

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]

text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200
        )

raw_documents = PyPDFLoader('italy_guide.pdf').load()
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings())

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

llm = ChatOpenAI()
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=db.as_retriever(), memory=memory, verbose=True)
print(qa_chain.run({'question':'Give me some review about the Pantheon'}))


#custom prompt
from langchain.prompts.prompt import PromptTemplate

custom_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question. 
If you cannot find the answer in the document provided, ignore the document and answer anyway.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""

CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)

# memory = ConversationBufferMemory(
#             memory_key='chat_history',
#             return_messages=True
#         )


qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=db.as_retriever(), condense_question_prompt=CUSTOM_QUESTION_PROMPT, memory=memory, verbose=True)
print(qa_chain.run({'question':'What can I visit in India?'}))

# create tools
from langchain.agents.agent_toolkits import create_retriever_tool

tool = create_retriever_tool(
    db.as_retriever(), 
    "italy_travel",
    "Searches and returns documents regarding Italy."
)
tools = [tool]

# memory = ConversationBufferMemory(
#             memory_key='chat_history',
#             return_messages=True
#         )

from langchain.agents.agent_toolkits import create_conversational_retrieval_agent

# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI(temperature = 0)

agent_executor = create_conversational_retrieval_agent(llm, tools, memory_key='chat_history', verbose=True)

print(agent_executor({"input": "hi, i'm Vale"}))
print(agent_executor({"input": "Tell me something about Pantheon"}))

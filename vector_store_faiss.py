import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]
# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader('./data/dialogue.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, separator = "\n",)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings())

#now lets use the vector store to do a similaruty search
query = "What is the reason for calling?"
docs = db.similarity_search(query)
print(docs[0].page_content)

# lets try to use the vector store as the back bone for a vector store retriever
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)
query = "What was the reason of the call?"
print(qa.run(query))
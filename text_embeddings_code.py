import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]
embeddings_model = OpenAIEmbeddings(model ='text-embedding-ada-002' )
embeddings = embeddings_model.embed_documents(
  [
    "Good morning!",
    "Oh, hello!",
    "I want to report an accident",
    "Sorry to hear that. May I ask your name?",
    "Sure, Mario Rossi."
  ]
)
print("Embed documents:")
print(f"Number of vector: {len(embeddings)}; Dimension of each vector: {len(embeddings[0])}")
embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
print("Embed query:")
print(f"Dimension of the vector: {len(embedded_query)}")
print(f"Sample of the first 5 elements of the vector: {embedded_query[:5]}")
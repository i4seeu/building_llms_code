import os
from dotenv import find_dotenv, load_dotenv
import openai
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
## data connections
load_dotenv(find_dotenv()) # load all the environmental variables
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0.7)
#print(llm('tell me a joke'))

print("+++++++++++ data connections code +++++++++++++++++++")
from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path='./data/sample.csv')
data = loader.load()
print(data)

## the  below code talks about the text splitters
with open('./data/mountain.txt') as f:
    mountain = f.read()
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    length_function = len
)
texts = text_splitter.create_documents([mountain])
# lets check the splitted texts
#print(texts)

# lets get the texts splitted in the documens
for text in texts:
    print(text)
# print(texts[0])
# print(texts[1])
# print(texts[2])
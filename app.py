## import all the necessary libraries
import warnings
warnings.filterwarnings('ignore')
import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv(find_dotenv()) # load all the environmental variables
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

llm = OpenAI(temperature=0.7)
# an example of an LLM
print(llm.predict("what is the weather in WA DC"))
print("==============================")
#an example of chat model
prompt = "How old is the Universe"
messages = [HumanMessage(content=prompt)]
chat_model = ChatOpenAI(temperature = 0.7)
#print(chat_model.predict("what is the weather in WA DC"))
print(chat_model.predict_messages(messages).content)






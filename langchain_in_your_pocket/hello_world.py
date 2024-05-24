import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

## name generator application

prompt = PromptTemplate.from_template("Give {number} names for an {domain} startup?")
llm = OpenAI()
chain = LLMChain(llm=llm,prompt=prompt)

print(chain.run({'number':'5','domain':'cooking'})) 
print(chain.run({'number':'2','domain':'AI'}))

## text preprocessing application

prompt2 = PromptTemplate.from_template("Preprocess the given text by following the given steps in sequence. Follow only those steps that have a yes against them. Remove Number:{number},Remove punctuations : {punc} ,Word stemming : {stem}.Output just the preprocessed text. Text : {text}")

chain2 = LLMChain(llm=llm,prompt=prompt2)

print(chain2.run({'text':'Hey!! I got 12 out of 20 in Swimming', 'number': 'yes', 'punc':'yes', 'stem':'no'}))
print(chain2.run({'text':'22 13B is my flat no. Rohit will be joining us for the party', 'number':'yes', 'punc':'no', 'stem':'yes'}))

## story teller
prompt3 = PromptTemplate.from_template(" Complete a {length} story using the given beginning. The genre should be {genre} and the story should have an apt ending. Beginning: {text}")
chain3 = LLMChain(llm=llm,prompt=prompt3)

print('\n'.join(chain3.run({'length':'short','genre':'horror','text':'Once there was a coder'}).replace('\n','.').split('.')))
print('\n'.join(chain3.run({'length':'short','genre':'rom-com','text':'And the Queen died'}).replace('\n','.').split('.')))
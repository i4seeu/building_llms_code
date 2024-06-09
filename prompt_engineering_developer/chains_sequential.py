import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

#==== Using OpenAI Chat API =======
llm_model = "gpt-3.5-turbo"

# chat = ChatOpenAI(temperature=0.9, model=llm_model)
open_ai = OpenAI(temperature=0.7)


template = """ 
 As a children's book writer, please come up with a simple and short (90 words)
 lullaby based on the location
 {location}
 and the main character {name}
 
 STORY:
"""

prompt = PromptTemplate(input_variables=["location", "name"],
                        template=template)

chain_story = LLMChain(llm=open_ai, prompt=prompt, 
                       output_key="story",
                       verbose=True)
story = chain_story({"location": "Zanzibar", "name": "Maya"})
# print(story['text'])

# ======= Sequential Chain =====
# chain to translate the story to Portuguese
template_update = """
Translate the {story} into {language}.  Make sure 
the language is simple and fun.

TRANSLATION:
"""

prompt_translate = PromptTemplate(input_variables=["story", "language"],
                                  template=template_update)

chain_translate = LLMChain(
    llm=open_ai,
    prompt=prompt_translate,
    output_key="translated"
)


# ==== Create the Sequential Chain ===
overall_chain = SequentialChain(
    chains=[chain_story, chain_translate],
    input_variables=["location", "name", "language"],
    output_variables=["story", "translated"], # return story and the translated variables!
    verbose=True
)

response = overall_chain({"location": "Magical", 
                          "name": "Karyna",
                          "language": "Russian"
                          })
print(f"English Version ====> { response['story']} \n \n")
print(f"Translated Version ====> { response['translated']}")
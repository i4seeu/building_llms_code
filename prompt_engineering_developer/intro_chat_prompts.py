import os
from openai import OpenAI
from dotenv import load_dotenv
#from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
load_dotenv()
#os.environ["SERPAPI_API_KEY"]
os.environ["OPENAI_API_KEY"]

llm_model = 'gpt-4'


openai = OpenAI()

def get_completion(prompt, model=llm_model):
    messages = [{"role":"user","content":prompt}]
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        temperature=0,
    )
    return response.choices[0].message.content

# Transalate text, review

customer_review =""" 
Your product is terrible! I don't know how you were able to get this to the market.
I don't want this! Actually no one should want this. Seriously! Give me money now!
"""
language ="Chichewa"
prompt =  f""" 
Rewrite the following {customer_review} in  a polite tone, and then please translate the new review message into {language}
"""
review_message = get_completion(prompt)
print(review_message)


# ========== using langchain and prompts templates - Still ChatAPI ===========
chat_model = ChatOpenAI(temperature=0.7,model=llm_model)
template_string = """
Translate the following text {customer_review} into {language} in a polite tone
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

translation_message = prompt_template.format_messages(
    customer_review = customer_review,
    language=language
)

response = chat_model(translation_message)
print(response.content)
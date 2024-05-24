import torch
import transformers
import os
from dotenv import load_dotenv
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
#from langchain_openai import OpenAI
from langchain.chains import LLMChain
## load the necessary Keys
load_dotenv()
os.environ["OPENAI_API_KEY"]

model = "EleutherAI/gpt-neo-125m"
#tokenizer = transformers.AutoTokenizer.from_pretrained(model)
tokenizer = transformers.AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
"text-generation",
model=model,
tokenizer=tokenizer,
torch_dtype=torch.bfloat16,
trust_remote_code=True,
max_length=200,
do_sample=True,
top_k=10,
num_return_sequences=1,
eos_token_id=tokenizer.eos_token_id,
pad_token_id=tokenizer.eos_token_id,
)


prompt=PromptTemplate.from_template("Tell me about {entity}")
llm = HuggingFacePipeline(pipeline=pipeline)
chain = LLMChain(llm=llm,prompt=prompt)

print('\n'.join(chain.run('humans').replace('\n','.').split('.')))
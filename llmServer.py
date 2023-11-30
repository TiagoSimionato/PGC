from fastapi import FastAPI
from langchain.llms.gpt4all import GPT4All
from langchain.prompts import PromptTemplate
from langserve import add_routes
import sys

####################
#LangChain LLM Setup
####################

#Path to weights
PATH = sys.argv[1] if (len(sys.argv) > 1) else './gpt4all-falcon-q4_0.gguf'

template = PromptTemplate.from_template(
  "{promot}"
)

chain = template | GPT4All(model=PATH, verbose=True)

###############
#Rest API Setup
###############

app = FastAPI(
  title='LangChain Server',
  version='1.0',
  description='Simple LLM API Provider',
)

add_routes(
  app,
  chain,
  path='/query'
)

if __name__ == '__main__':
  import uvicorn

  uvicorn.run(app, host='localhost', port=8000)
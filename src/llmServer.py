from fastapi import FastAPI
from langchain.llms.gpt4all import GPT4All
from langchain.prompts import PromptTemplate
from langserve import add_routes
from langchain.evaluation import load_evaluator
from configs import LARGER_MODEL_PATH, MEDIUM_MODEL_PATH, SMALLER_MODEL_PATH
import sys

####################
#LangChain LLM Setup
####################

path_resolve = ''
if (len(sys.argv) > 1):
  input = int(sys.argv[1])

  options = [1, 2, 3]

  path_mapping = {
    1: SMALLER_MODEL_PATH,
    2: MEDIUM_MODEL_PATH,
    3: LARGER_MODEL_PATH,
  }

  if input in options:
    path_resolve = path_mapping[input]

#Path to weights
PATH = path_resolve if (path_resolve != '') else LARGER_MODEL_PATH

template = PromptTemplate.from_template(
  "{prompt}"
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
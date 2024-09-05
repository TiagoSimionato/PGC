from constants import REQUIREMENTS

EXAMPLE_CONTEXT = '''\'\'\'Software Requirements Specification
Example Name

Introduction
Purpose

The purpose of this document is to present a detailed description about how the software should work. It describes which functionalities it should have. The document serves as a guide for the stakeholders and software developers alike.

General Description

This is an example description of the overall purpose of the software

Functional Requirements Description

Use cases

- The User needs to login

There should be a button taking the user to a sign in page, where they can inform their user and password and a confirmation button, which sends this information to the server side so it can validade if the provided information exists on the database

- The User needs to log out

The shoud be a button when pressed, deletes all token information from the user device, so the aplication does not think the user is the one previously signed.
\'\'\'

based on the requirements document provided, list every test case scenario, comma separated'''
EXPECTED_ANSWER = 'login, logout'
CONTEXT = REQUIREMENTS + '\n\nbased on the requirements document provided, list every test case scenario, comma separated'

from secrets.key import API_KEY

from langchain_google_genai import ChatGoogleGenerativeAI

from configs import OUTPUT_PATH
from prompt import requirements_template
from utils import save

model_name = 'requirements_prompt'
model = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=API_KEY)
prompt = requirements_template(context=CONTEXT, example_context=EXAMPLE_CONTEXT, expected_answer=EXPECTED_ANSWER)
for i in range(0, 10):
  response: str = ''
  for chunk in model.stream(prompt):
    response += chunk.content

  save(content=response, file_name=model_name, output_path=OUTPUT_PATH)

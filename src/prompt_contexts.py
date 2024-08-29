from constants import FINAL_QUESTION
from utils import BASE_CODE


def tested_features_chunk(tested_features: list[str]):
  if (len(tested_features) > 0):
    return f'There are tests covering the following features: {', '.join(tested_features)}'
  else :
    return 'No features are tested yet'

def ui_info_context(app_name: str, features: list[str], tested_features: list[str], example: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. The application needs the following features to be tested:\n{features}\n{tested_chunk}. It\'s your job to select one of the features not yet tested and write a function that will belong to the TestAppium class. You have the following information extracted from the ui represening buttons and text views:

\'\'\'
{example}
\'\'\'

{FINAL_QUESTION}'''

def requirements_context(app_name: str, tested_features: list[str], requirements: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. It\'s your job to select one the features not yet tested and write a function that will belong to the TestAppium class. Next, to help you with this task, there is a document between triple quotes describing the requirements for this software, meaning there must be a test with the appropriate assertions for each requirement in the list.

\'\'\'
{requirements}
\'\'\'

{FINAL_QUESTION}'''

def code_context(app_name: str, tested_features: list[str]):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. To help you start, your coworkers already gave you the following Python code:

\'\'\'
{BASE_CODE}
\'\'\'

It\'s your job to select one of the features not yet tested and write a function that will belong to the TestAppium class. You have the following information extracted from the ui represening buttons and text views:
{FINAL_QUESTION}'''

def ui_requirements_context(app_name: str, tested_features: list[str], requirements: str, example: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. It\'s your job to select one of the features not yet tested and write a function that will belong to the TestAppium class. Next there is a document between triple quotes describing the requirements for this software, meaning there must be a test for each requirement in the list.

\'\'\'
{requirements}
\'\'\'

For further assistance, there is also a list with information extracted from the ui represening buttons and text views:

\'\'\'
{example}
\'\'\'

{FINAL_QUESTION}'''

def ui_info_code_context(app_name: str, tested_features: list[str], example: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. To help you start, your coworkers already gave you the following Python code:

\'\'\'
{BASE_CODE}
\'\'\'

It\'s your job to select one of the features not yet tested and write a function that will belong to the TestAppium class. You have the following information extracted from the ui represening buttons and text views:

\'\'\'
{example}
\'\'\'

{FINAL_QUESTION}'''

def requirements_code_context(app_name: str, tested_features: list[str], requirements: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. To help you start, your coworkers already gave you the following Python code:

\'\'\'
{BASE_CODE}
\'\'\'

It\'s your job to select one the features not yet tested and write a function that will belong to the TestAppium class. Next, to help you with this task, there is a document between triple quotes describing the requirements for this software, meaning there must be a test with the appropriate assertions for each requirement in the list.

\'\'\'
{requirements}
\'\'\'

{FINAL_QUESTION}'''

def ui_requirements_code_context(app_name: str, tested_features: list[str], requirements: str, example: str):
  tested_chunk = tested_features_chunk(tested_features)

  return f'''You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. {tested_chunk}. To help you start, your coworkers already gave you the following Python code:

\'\'\'
{BASE_CODE}
\'\'\'

It\'s your job to select one of the features not yet tested and write a function that will belong to the TestAppium class. Next there is a document between triple quotes describing the requirements for this software, meaning there must be a test for each requirement in the list.

\'\'\'
{requirements}
\'\'\'

For further assistance, there is also a list with information extracted from the ui represening buttons and text views:

\'\'\'
{example}
\'\'\'

{FINAL_QUESTION}'''
from constants import CALCULATOR_UI_INFO, FINAL_QUESTION, REQUIREMENTS
from utils import BASE_CODE, CODE_EXAMPLE_SUB, CODE_EXAMPLE_SUM, load


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

def few_shot_template(ui_info, context, app_name: str, features: list[str], tested_features: list[str]):
  return f'''Question:
{context(app_name='Calculator', features=features, tested_features=[], example=CALCULATOR_UI_INFO)}
Answer:
TESTED FEATURES: sum
\'\'\'
{CODE_EXAMPLE_SUM}
\'\'\'
Question:
{context(app_name='Calculator', features=features, tested_features=['sum'], example=CALCULATOR_UI_INFO)}
Answer:
TESTED FEATURES: sum, subtraction
\'\'\'
{CODE_EXAMPLE_SUB}
\'\'\'

Question:
{context(app_name=app_name, features=features, tested_features=tested_features, example=ui_info)}
Answer:
'''

def prompt_template(ui_info, app_name: str, features: list[str], tested_features: list[str], strategy = 'UI'):
  def dynamic_context(app_name: str, features: list[str], tested_features: list[str], example) :
    if (strategy == 'UI'):
      return ui_info_context(app_name=app_name, features=features, tested_features=tested_features, example=example)
    elif (strategy == 'REQ'):
      return requirements_context(app_name=app_name, requirements=REQUIREMENTS, tested_features=tested_features)
    elif (strategy == 'CODE'):
      return code_context(app_name=app_name, tested_features=tested_features)
    elif (strategy == 'UI_REQ'):
      return ui_requirements_context(app_name=app_name, tested_features=tested_features, requirements=REQUIREMENTS, example=example)
    elif (strategy == 'UI_CODE'):
      return ui_info_code_context(app_name=app_name, tested_features=tested_features, example=example)
    elif (strategy == 'REQ_CODE'):
      return requirements_code_context(app_name=app_name, requirements=REQUIREMENTS, tested_features=tested_features)
    elif (strategy == 'UI_REQ_CODE'):
      return ui_requirements_code_context(app_name=app_name, tested_features=tested_features, requirements=REQUIREMENTS, example=example)
    else :
      raise('Not a valid strategy')
    
  return few_shot_template(ui_info=ui_info, context=dynamic_context, app_name=app_name, features=features, tested_features=tested_features)

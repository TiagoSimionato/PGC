from utils import BASE_CODE, CODE_EXAMPLE_SUB, CODE_EXAMPLE_SUM, load

CALCULATOR_UI_INFO = f'''{{'buttons': [{{'text': 'DEG', 'tag_name': 'degree mode'}}, {{'text': 'INV', 'tag_name': 'show inverse functions'}}, {{'text': 'RAD', 'tag_name': 'switch to radians'}}, {{'text': 'sin', 'tag_name': 'sine'}}, {{'text': 'cos', 'tag_name': 'cosine'}}, {{'text': 'tan', 'tag_name': 'tangent'}}, {{'text': '%', 'tag_name': 'percent'}}, {{'text': 'ln', 'tag_name': 'natural logarithm'}}, {{'text': 'log', 'tag_name': 'logarithm'}}, {{'text': '√', 'tag_name': 'square root'}}, {{'text': '^', 'tag_name': 'power'}}, {{'text': 'π', 'tag_name': 'pi'}}, {{'text': 'e', 'tag_name': "Euler's number"}}, {{'text': '(', 'tag_name': 'left parenthesis'}}, {{'text': ')', 'tag_name': 'right parenthesis'}}, {{'text': '!', 'tag_name': 'factorial'}}, {{'text': '7', 'tag_name': None}}, {{'text': '8', 'tag_name': None}}, {{'text': '9', 'tag_name': None}}, {{'text': '4', 'tag_name': None}}, {{'text': '5', 'tag_name': None}}, {{'text': '6', 'tag_name': None}}, {{'text': '1', 'tag_name': None}}, {{'text': '2', 'tag_name': None}}, {{'text': '3', 'tag_name': None}}, {{'text': '0', 'tag_name': None}}, {{'text': '.', 'tag_name': 'point'}}, {{'text': '÷', 'tag_name': 'divide'}}, {{'text': '×', 'tag_name': '×'}}, {{'text': '−', 'tag_name': 'minus'}}, {{'text': '+', 'tag_name': 'plus'}}, {{'text': '=', 'tag_name': 'equals'}}], 'textViews': [{{'text': '', 'tag_name': 'No formula'}}, {{'text': '', 'tag_name': 'No result'}}]}}'''

def question_context(app_name: str, features: list[str], tested_features: list[str]):
  tested_chunk: str = ''
  if (len(tested_features) > 0):
    tested_chunk = f'There are tests covering the following features: {tested_features}'
  else :
    tested_chunk = 'No features are tested yet'

  return f'You are a Software Test Engineer and there\'s an Android aplication called {app_name} you have to write tests for. The application needs the following features to be tested:\n{features}\n{tested_chunk}. To help you start, your coworkers already gave you the following base code: \n```\n{BASE_CODE}```\n\nIt\'s your job to select one of these features and write a function that will belong to the TestAppium class. You have the following information extracted from the ui represening buttons and text views:'

FINAL_QUESTION = 'Your Python function should correctly test the selected feature, making sure it works as exected. The code should use Appium and the python library unittest. Infer what assertions the respective tests need based on the provided information. Every test needs at least one assertion. Whenever the expected result would be a decimal number, use assertAlmostEqual for the assertion with a delta = 0.0001. Once all tests are executed, every button should be clicked at least once. Before the code should be a list informing the total features tested so far.'

def prompt_template(ui_info, app_name: str, features: list[str], tested_features: list[str]):
  return f'''Question:
{question_context(app_name='Calculator', features=features, tested_features=[])}
{CALCULATOR_UI_INFO}
{FINAL_QUESTION}
Answer:
TESTED FEATURES: sum;
```
{CODE_EXAMPLE_SUM}
```
Question:
{question_context(app_name='Calculator', features=features, tested_features=['sum'])}
{CALCULATOR_UI_INFO}
{FINAL_QUESTION}
Answer:
TESTED FEATURES: sum, subtraction;
```
{CODE_EXAMPLE_SUB}
```

Question:
{question_context(app_name=app_name, features=features, tested_features=tested_features)}
{ui_info}
{FINAL_QUESTION}
Answer:
'''

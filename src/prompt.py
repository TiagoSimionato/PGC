from utils import load


def question_context(appName: str, appDescripton: str):
  return f'You are a Software Test Engineer and there\'s an Android aplication called {appName} you have to write tests for. {appDescripton}. You have the following information extracted from the ui represening buttons and text views:'

FINAL_QUESTION = 'Write a Python code able to test the interface and make sure it works as expected. The code should use Appium and the python library unittest. Infer the features that should be tested and what assertions the respective tests need based on the provided information and add as many tests as needed. Every test needs at least one assertion. Once all tests are executed, every button should be clicked at least once.'

code_example = load('./src/example_code.py')

def prompt_template(button_text_list, appName, appDescription):
  return f'''Question:
{question_context(appName='Calculator', appDescripton='It performs arithmetic operations on numbers so the user can quickly calculate the result of complex operations')}
{{'buttons': [{{'text': 'DEG', 'tag_name': 'degree mode'}}, {{'text': 'INV', 'tag_name': 'show inverse functions'}}, {{'text': 'RAD', 'tag_name': 'switch to radians'}}, {{'text': 'sin', 'tag_name': 'sine'}}, {{'text': 'cos', 'tag_name': 'cosine'}}, {{'text': 'tan', 'tag_name': 'tangent'}}, {{'text': '%', 'tag_name': 'percent'}}, {{'text': 'ln', 'tag_name': 'natural logarithm'}}, {{'text': 'log', 'tag_name': 'logarithm'}}, {{'text': '√', 'tag_name': 'square root'}}, {{'text': '^', 'tag_name': 'power'}}, {{'text': 'π', 'tag_name': 'pi'}}, {{'text': 'e', 'tag_name': "Euler's number"}}, {{'text': '(', 'tag_name': 'left parenthesis'}}, {{'text': ')', 'tag_name': 'right parenthesis'}}, {{'text': '!', 'tag_name': 'factorial'}}, {{'text': '7', 'tag_name': None}}, {{'text': '8', 'tag_name': None}}, {{'text': '9', 'tag_name': None}}, {{'text': '4', 'tag_name': None}}, {{'text': '5', 'tag_name': None}}, {{'text': '6', 'tag_name': None}}, {{'text': '1', 'tag_name': None}}, {{'text': '2', 'tag_name': None}}, {{'text': '3', 'tag_name': None}}, {{'text': '0', 'tag_name': None}}, {{'text': '.', 'tag_name': 'point'}}, {{'text': '÷', 'tag_name': 'divide'}}, {{'text': '×', 'tag_name': '×'}}, {{'text': '−', 'tag_name': 'minus'}}, {{'text': '+', 'tag_name': 'plus'}}, {{'text': '=', 'tag_name': 'equals'}}], 'textViews': [{{'text': '', 'tag_name': 'No formula'}}, {{'text': '', 'tag_name': 'No result'}}]}}
{FINAL_QUESTION}
Answer:
```
{code_example}
```
Question:
{question_context(appName=appName, appDescripton=appDescription)}
{button_text_list}
{FINAL_QUESTION}
Answer:
'''

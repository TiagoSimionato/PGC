from utils import load

def question_context(appName: str, appDescripton: str):
  return f'You are a Software Test Engineer and there\'s an Android aplication called {appName} you have to write tests for. {appDescripton}. You know there are buttons in it\'s interface with the following texts:'

FINAL_QUESTION = 'Write a Python code able to test the interface and make sure it works as expected. The code should use Appium and the python library unittest. Infer the features that should be tested and what assertions the respective tests need based on the provided information and add as many tests as needed. Every test needs at least one assertion. Once all tests are executed, every button should be clicked at least once.'

code_example = load('./src/example_code.py')

def prompt_template(button_text_list, appName, appDescription):
  return f'''Question:
{question_context(appName='Calculator', appDescripton='It performs arithmetic operations on numbers so the user can quickly calculate the result of complex operations')}
['DEG', 'INV', 'RAD', 'sin', 'cos', 'tan', '%', 'ln', 'log', '√', '^', 'π', 'e', '(', ')', '!', '7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '÷', '×', '−', '+', '=']
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

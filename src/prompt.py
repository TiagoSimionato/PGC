from utils import load

QUESTION_CONTEXT = 'You are a Software Test Engineer and there\'s an Android aplication you have to write tests for. You know there are buttons in it\'s interface with the following texts:'

FINAL_QUESTION = 'Write a Python code able to test the interface using Appium and the python library called unittest. Infer the features that should be tested based on the provided ui info and add as many tests to the code as needed. Every test needs at least one assertion.'

code_example = load('./src/example_code.py')

def prompt_template(button_text_list):
  return f'''Question:
{QUESTION_CONTEXT}
['Battery', 'Settings']
{FINAL_QUESTION}
Answer:
```
{code_example}
```
Question:
{QUESTION_CONTEXT}
{button_text_list}
{FINAL_QUESTION}
Answer:
'''

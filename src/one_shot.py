from constants import CALCULATOR_UI_INFO
from utils import CODE_EXAMPLE_SUB, CODE_EXAMPLE_SUM


def one_shot_template(example_context: str, expected_answer: str, context: str):
  return f'''Question:
{example_context}

Answer:
{expected_answer}

Question:
{context}

Answer:
'''

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
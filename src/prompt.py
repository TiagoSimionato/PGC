from constants import REQUIREMENTS
from one_shot import few_shot_template, one_shot_template
from prompt_contexts import (code_context, requirements_code_context,
                             requirements_context, ui_info_code_context,
                             ui_info_context, ui_requirements_code_context,
                             ui_requirements_context)


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

def requirements_template(example_context, expected_answer, context):
  return one_shot_template(example_context=example_context, expected_answer=expected_answer, context=context)

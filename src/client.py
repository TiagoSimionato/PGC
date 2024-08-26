import argparse

from configs import OUTPUT_PATH
from prompt import prompt_template
from ui_parser import parse
from utils import (BASE_CODE, CODE_EXAMPLE_SUB, CODE_EXAMPLE_SUM, FINAL_LINES,
                   load, parseResponse, save)

ap = argparse.ArgumentParser()
ap.add_argument('-ap', '--appiumPort', type=int, default=4723, help='Port to appium server running on localhost')
ap.add_argument('-m', '--model', type=int, default=1, help='Int representing the model choice. 1 stands for gemini and 2 for local models')
ap.add_argument('-op', '--outputPath', default=OUTPUT_PATH, type=str, help='String indicating where generated anwswers will be stored')
ap.add_argument('-lmn', '--localModelName', default='wizard', type=str, help='Used to name the output file when using local models')
ap.add_argument('-uc', '--useCache', default=False, type=bool, help='Indicates whether the UI info should be extracted or search from a local cache')
ap.add_argument('-s', '--strategy', type=str, default='UI', help='Strategy used to generate the prompt for the llm')
args = vars(ap.parse_args())

output_path = args['outputPath']
strategy=args['strategy']

capabilities = dict(
  platformName='Android',
  automationName='uiautomator2',
  deviceName='avd',
  appPackage='com.google.android.calculator',
  appActivity='com.android.calculator2.Calculator',
  language='en',
  locale='US'
)

ui_elements = load('./cache/com.google.android.calculator.txt')
if (not args['useCache']):
  ui_elements = parse(capabilities=capabilities, appium_port=args['appiumPort'])

CALCULATOR_FEATURES = ['sum', 'subtraction', 'multiplication', 'division', 'percentage', 'exponentiation', 'rooting', 'multiplicative inverse', 'change of sign', 'logarithm', 'sen', 'cos', 'tan', 'absolute value']
tested_features : list[str] = []
tested_features_iteration = ''

generated_code: str = BASE_CODE + '\n' + CODE_EXAMPLE_SUM + '\n' + CODE_EXAMPLE_SUB
last_tested_features_amount = 0
times_tested_features_not_increased = 0

while(times_tested_features_not_increased <= 3):
  prompt = prompt_template(ui_info=ui_elements, app_name='Calculator', features=CALCULATOR_FEATURES, tested_features=tested_features, strategy=strategy)

  if (args['model'] == 1):
    from secrets.key import API_KEY

    from langchain_google_genai import ChatGoogleGenerativeAI

    model_name = strategy
    model = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=API_KEY)
    response: str = ''
    for chunk in model.stream(prompt):
      response += chunk.content
  else:
    from langserve import RemoteRunnable

    model_name = args['localModelName']

    remote_chain = RemoteRunnable('http://localhost:8000/query/')
    response = remote_chain.invoke({"prompt" : prompt})

  [tested_features_list, code] = parseResponse(response)
  tested_features = tested_features_list
  tested_features_iteration += ','.join(tested_features) + '\n\n'
  generated_code += code
  print(f'Got response. Total tested features: {len(tested_features)}')
  if (len(tested_features) == last_tested_features_amount):
    times_tested_features_not_increased += 1
  else:
    times_tested_features_not_increased = 0
  last_tested_features_amount = len(tested_features)

generated_code += FINAL_LINES
print(generated_code)
content = f'''PROMPT:
{prompt}

RESPONSE:
{tested_features_iteration}
{generated_code}
'''
save(content=content, file_name=model_name, output_path=output_path)
import argparse

from configs import OUTPUT_PATH
from prompt import prompt_template
from ui_parser import parse
from utils import save

ap = argparse.ArgumentParser()
ap.add_argument('-ap', '--appiumPort', type=int, default=4723, help='Port to appium server running on localhost')
ap.add_argument('-m', '--model', type=int, default=1, help='Int representing the model choice. 1 stands for gemini and 2 for local models')
args = vars(ap.parse_args())

capabilities = dict(
  platformName='Android',
  automationName='uiautomator2',
  deviceName='avd',
  appPackage='com.google.android.calculator',
  appActivity='com.android.calculator2.Calculator',
  language='en',
  locale='US'
)

ui_elements = parse(capabilities=capabilities, appium_port=args['appiumPort'])

prompt = prompt_template(button_text_list=ui_elements['button'])

if (args['model'] == 1):
  from secrets.key import API_KEY

  from models.gemini import invoke_gemini

  model_name='gemini'

  response = invoke_gemini(prompt=prompt, api_key=API_KEY)
else:
  from langserve import RemoteRunnable

  model_name='falcon'

  remote_chain = RemoteRunnable('http://localhost:8000/query/')
  response = remote_chain.invoke({"prompt" : prompt})

print(response)
content = f'''PROMPT:
{prompt}

RESPONSE:
{response}
'''
save(content=content, file_name=model_name, output_path=OUTPUT_PATH)
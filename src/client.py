import argparse
import sys

from langserve import RemoteRunnable

from configs import OUTPUT_PATH
from prompt import prompt_template
from ui_parser import parse
from utils import save

model_name='falcon'

ap = argparse.ArgumentParser()
ap.add_argument('-ap', '--appiumPort', type=int, default=4723, help='Port to appium server running on localhost')
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

prompt = prompt_template(button_text_list=ui_elements)

#prompt = " ".join(sys.argv[1:]) if (len(sys.argv) > 1) else 'say hello'

remote_chain = RemoteRunnable('http://localhost:8000/query/')
response = remote_chain.invoke({"prompt" : prompt})

print(response)
content = f'''PROMPT:
{prompt}

RESPONSE:
{response}
'''
save(content=content, file_name=model_name, output_path=OUTPUT_PATH)
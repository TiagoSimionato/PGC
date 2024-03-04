import argparse
import sys

from langserve import RemoteRunnable

from ui_parser import parse

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

ui_elements = parse(capabilities=capabilities, appiumPort=args['appiumPort'])

#prompt = " ".join(sys.argv[1:]) if (len(sys.argv) > 1) else 'say hello'

# prompt = f' \\
# ADASD \\
# ASDAS as
# '

# remote_chain = RemoteRunnable('http://localhost:8000/query/')
# response = remote_chain.invoke({"prompt" : prompt})

# print(response)
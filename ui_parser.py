from collections import defaultdict

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
  platformName='Android',
  automationName='uiautomator2',
  deviceName='avd',
  appPackage='com.google.android.calculator',
  appActivity='com.android.calculator2.Calculator',
  language='en',
  locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

def parse(appiumPort = 4723):
  url = f'http://192.168.15.35:{appiumPort}'
  driver = webdriver.Remote(command_executor=url, options=capabilities_options)

  elements = ['//android.widget.Button','//android.widget.TextView']
  names = ['button', 'textView']

  result = defaultdict(list)

  for i in range(len(elements)):
    search = driver.find_elements(by=AppiumBy.XPATH, value=elements[i])
    result[names[i]] = search

  driver.quit()
  return result
import json
import os
from collections import defaultdict

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from configs import CACHE_PATH


def getText(item):
  return item.get_attribute(name='text')

def parse(capabilities,appiumPort = 4723, shouldCache= True):
  capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
  url = f'http://192.168.15.35:{appiumPort}'
  driver = webdriver.Remote(command_executor=url, options=capabilities_options)

  elements = ['//android.widget.Button','//android.widget.TextView']
  names = ['button', 'textView']

  result = defaultdict(list)

  page_source = driver.page_source

  for i in range(len(elements)):
    searchItems = driver.find_elements(by=AppiumBy.XPATH, value=elements[i])
    itemsText = list(map(getText, searchItems))
    result[names[i]] = itemsText
  
  if (shouldCache):
    if  (not os.path.isdir(CACHE_PATH)):
      os.mkdir(CACHE_PATH)
    appName = capabilities['appPackage']
    savePath = f'{CACHE_PATH}/{appName}.txt'
    with open(savePath, 'w', encoding='utf-8') as f:
      f.write(result['button'].__str__())

  driver.quit()
  return result
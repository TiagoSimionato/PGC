import json
import os
from collections import defaultdict

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from configs import CACHE_PATH

def parse(capabilities, appium_port = 4723, should_cache= True):
  capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
  url = f'http://192.168.15.35:{appium_port}'
  driver = webdriver.Remote(command_executor=url, options=capabilities_options)

  elements = ['//android.widget.Button','//android.widget.TextView']
  names = ['button', 'textView']

  result = defaultdict(list)

  page_source = driver.page_source

  for i in range(len(elements)):
    search_items = driver.find_elements(by=AppiumBy.XPATH, value=elements[i])
    items_text = list(map(getText, search_items))
    result[names[i]] = items_text
  
  if (should_cache):
    if  (not os.path.isdir(CACHE_PATH)):
      os.mkdir(CACHE_PATH)
    app_name = capabilities['appPackage']
    save_path = f'{CACHE_PATH}/{app_name}.txt'
    with open(save_path, 'w', encoding='utf-8') as f:
      f.write(result['button'].__str__())

  driver.quit()
  return result
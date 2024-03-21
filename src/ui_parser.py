import os
from collections import defaultdict

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from configs import CACHE_PATH
from utils import getText


def parse(capabilities, appium_port = 4723, should_cache= True):
  capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
  url = f'http://192.168.15.35:{appium_port}'
  driver = webdriver.Remote(command_executor=url, options=capabilities_options)

  element_types = ['//android.widget.Button','//android.widget.TextView']
  names = ['buttons', 'textViews']

  page_source = driver.page_source

  result = {}
  for i in range(len(element_types)):
    search_items = driver.find_elements(by=AppiumBy.XPATH, value=element_types[i])

    items = []
    for j in range(len(search_items)):
      atribs = {}
      atribs['text'] = search_items[j].text
      atribs['tag_name'] = search_items[j].tag_name

      items.append(atribs)

    # items_text = list(map(getText, search_items))
    result[names[i]] = items
  
  if (should_cache):
    if  (not os.path.isdir(CACHE_PATH)):
      os.mkdir(CACHE_PATH)
    app_name = capabilities['appPackage']
    save_path = f'{CACHE_PATH}/{app_name}.txt'
    with open(save_path, 'w', encoding='utf-8') as f:
      f.write(result.__str__())

  driver.quit()
  return result
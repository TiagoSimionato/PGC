QUESTION_CONTEXT = 'You are a Software Test Engineer. Knowing there\'s an Android aplication you have to test and it has you know it\'s interface has buttons with the following texts:'

FINAL_QUESTION = 'Write a Python code able to test the interface using Appium and the python library called unittest'
#<android.widget.Button text="Battery" />
def prompt_template(button_text_list):
  return f'''Question:
{QUESTION_CONTEXT}
[Battery,Settings]
{FINAL_QUESTION}
Answer:
```
import argparse
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
platformName=\'Android\',
automationName=\'uiautomator2\',
deviceName=\'avd\',
appPackage=\'com.google.android.calculator\',
appActivity=\'com.android.calculator2.Calculator\',
language=\'en\',
locale=\'US\'
)
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
  def setUp(self) -> None:
    self.driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, options=capabilities_options)

  def tearDown(self) -> None:
    if self.driver:
      self.driver.quit()

  def test_find_battery(self) -> None:
    el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

  def test_find_settings(self) -> None:
    el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
    el.click()

  def test_dump(self) -> None:
    print(self.driver.page_source)

if __name__ == '__main__':
  unittest.main()
```
Question:
{QUESTION_CONTEXT}
{button_text_list}
{FINAL_QUESTION}
Answer:
'''
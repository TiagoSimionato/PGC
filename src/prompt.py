QUESTION_CONTEXT = 'You are a Software Test Engineer. Knowing there\'s an Android aplication you have to write tests for. You know it\'s interface has buttons with the following texts:'

FINAL_QUESTION = 'Write a Python code able to test the interface using Appium and the python library called unittest. Infer the features that should be tested based on the provided ui info and add ad many tests to the code as needed'
#<android.widget.Button text="Battery" />
def prompt_template(button_text_list):
  return f'''Question:
{QUESTION_CONTEXT}
['Battery', 'Settings']
{FINAL_QUESTION}
Answer:
```
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
    self.driver = webdriver.Remote(command_executor='http://192.168.15.35:4723', options=capabilities_options)

  def tearDown(self) -> None:
    if self.driver:
      self.driver.quit()

  def test_find_battery(self) -> None:
    el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

  def test_find_settings(self) -> None:
    el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
    el.click()

if __name__ == '__main__':
  unittest.main()
```
Question:
{QUESTION_CONTEXT}
{button_text_list}
{FINAL_QUESTION}
Answer:
'''
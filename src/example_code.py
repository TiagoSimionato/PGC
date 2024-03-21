import argparse
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

ap = argparse.ArgumentParser()
ap.add_argument('-ap', '--appiumPort', type=int, default=4723, help='Port to appium server running on localhost')
args = vars(ap.parse_args())

APPIUM_SERVER_URL =  f'http://192.168.15.35:{args['appiumPort']}'

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

class TestAppium(unittest.TestCase):
  def setUp(self) -> None:
    self.driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, options=capabilities_options)

  def tearDown(self) -> None:
    if self.driver:
      self.driver.quit()

  def test_sum(self) -> None:
    expr_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='No formula']")
    result_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='No result']")

    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="9"]').click()
    self.assertEqual(expr_text_view.text, '9')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="+"]').click()
    self.assertEqual(expr_text_view.text, '9+')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="2"]').click()
    self.assertEqual(expr_text_view.text, '9+2')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="="]').click()
    self.assertEqual(result_text_view.text, '11')

    self.assertEqual(expr_text_view.text, '11')


  def test_minus(self) -> None:
    expr_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='No formula']")
    result_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='No result']")
  
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="5"]').click()
    self.assertEqual(expr_text_view.text, '5')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="5"]').click()
    self.assertEqual(expr_text_view.text, '55')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="−"]').click()
    self.assertEqual(expr_text_view.text, '55−')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="3"]').click()
    self.assertEqual(result_text_view.text, '55−3')

    #Assertion
    self.assertEqual(expr_text_view.text, '52')

if __name__ == '__main__':
  unittest.main()
  
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
    self.expr_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='com.google.android.calculator:id/formula']")
    self.preview_text_view = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@*='com.google.android.calculator:id/result_preview']")

  def tearDown(self) -> None:
    if self.driver:
      self.driver.quit()

  def test_sum(self) -> None:
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="9"]').click()
    self.assertEqual(self.expr_text_view.text, '9')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="+"]').click()
    self.assertEqual(self.expr_text_view.text, '9+')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="2"]').click()
    self.assertEqual(self.expr_text_view.text, '9+2')
    self.assertEqual(self.preview_text_view.text, '11')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="="]').click()
    result_text_view = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@*='com.google.android.calculator:id/result_final']")
    self.assertEqual(result_text_view.text, '11')

  def test_minus(self) -> None:
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="5"]').click()
    self.assertEqual(self.expr_text_view.text, '5')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="4"]').click()
    self.assertEqual(self.expr_text_view.text, '54')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="−"]').click()
    self.assertEqual(self.expr_text_view.text, '54−')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="3"]').click()
    self.assertEqual(self.expr_text_view.text, '54−3')
    self.assertEqual(self.preview_text_view.text, '51')
    self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="="]').click()
    result_text_view = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@*='com.google.android.calculator:id/result_final']")
    self.assertEqual(result_text_view.text, '51')

if __name__ == '__main__':
  unittest.main()
  
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
    #Action
    button_nine = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="9"]')
    button_nine.click()
    button_plus = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="+"]')
    button_plus.click()
    button_two = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="2"]')
    button_two.click()

    #Assertion
    result = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="11"]')
    self.assertEqual(result.text, '11')

  def test_minus(self) -> None:
    #Action
    button_five = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="5"]')
    button_five.click()
    button_five.click()
    button_minus = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="-"]')
    button_minus.click()
    button_three = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="3"]')
    button_three.click()

    #Assertion
    result = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="52"]')
    self.assertEqual(result.text, '11')

if __name__ == '__main__':
  unittest.main()
  
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

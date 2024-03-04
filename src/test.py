print(f'''Question:
Knowing there\'s an interface for an Android aplication with the following buttons:
<Button>
Generate a Python code that is able to test the interface using Appium and the python library called unittest
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
```
''')
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'platformName':'Android',
    'automationName':'uiautomator2',
    'deviceName':'Samsung S9',
    'appPackage':'com.mill.android',
    'appActivity':'com.mill.android.MainActivity'
}

appium_server_url = 'http://localhost:4723'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

# Wait time for an element to be found or a command to be complete
driver.implicitly_wait(30)

# Finds and populates email field on Mill App
EmailField = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Email"]')
EmailField.click()
EmailField.send_keys('lpalomin@uwsuper.edu')

# Finds and populates password field on Mill App
PasswordField = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Password"]')
PasswordField.click()
PasswordField.send_keys('FakePassword2023')

# Clicks on sign in button
SignIn = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Sign in"]/android.view.ViewGroup')
SignIn.click()

time.sleep(5)

driver.quit()


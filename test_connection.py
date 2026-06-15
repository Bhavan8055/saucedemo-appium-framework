from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"

options.app_package = "com.saucelabs.mydemoapp.android"
options.app_wait_activity = "com.saucelabs.mydemoapp.android.view.activities.*"

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

print("Connected Successfully")
print("Current Package:", driver.current_package)

driver.quit()
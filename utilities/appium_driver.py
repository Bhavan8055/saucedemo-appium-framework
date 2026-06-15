from appium import webdriver
from config.config import (
    APPIUM_SERVER,
    PLATFORM_NAME,
    DEVICE_NAME,
    PLATFORM_VERSION,
    AUTOMATION_NAME,
    APP_PACKAGE,
    APP_ACTIVITY,
    NEW_COMMAND_TIMEOUT,
)


def create_driver():
    desired_capabilities = {
        "platformName": PLATFORM_NAME,
        "deviceName": DEVICE_NAME,
        "platformVersion": PLATFORM_VERSION,
        "automationName": AUTOMATION_NAME,
        "appPackage": APP_PACKAGE,
        "appActivity": APP_ACTIVITY,
        "newCommandTimeout": NEW_COMMAND_TIMEOUT,
        "autoGrantPermissions": True,
        "noReset": True,
    }

    driver = webdriver.Remote(command_executor=APPIUM_SERVER, desired_capabilities=desired_capabilities)
    return driver

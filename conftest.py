import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.logger import get_logger

logger = get_logger("DriverSetup")


@pytest.fixture(scope="function")
def driver():

    logger.info("Initializing Appium Driver...")

    options = UiAutomator2Options()

    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "Android")

    # Sauce Demo App
    options.set_capability(
        "appPackage",
        "com.saucelabs.mydemoapp.android"
    )

    options.set_capability(
        "appActivity",
        "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    )

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.implicitly_wait(5)

    yield driver

    logger.info("Closing test session...")
    driver.quit()
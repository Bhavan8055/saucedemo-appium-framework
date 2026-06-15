import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Appium / device settings
APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723/wd/hub")
PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
DEVICE_NAME = os.getenv("DEVICE_NAME", "Pixel_3_API_33")
AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UiAutomator2")
APP_PACKAGE = os.getenv("APP_PACKAGE", "com.example.movieapp")
APP_ACTIVITY = os.getenv("APP_ACTIVITY", ".MainActivity")
PLATFORM_VERSION = os.getenv("PLATFORM_VERSION", "13.0")
NEW_COMMAND_TIMEOUT = int(os.getenv("NEW_COMMAND_TIMEOUT", "300"))

# Paths
REPORT_PATH = os.path.join(BASE_DIR, "reports")
SCREENSHOT_PATH = os.path.join(BASE_DIR, "screenshots")
LOG_PATH = os.path.join(BASE_DIR, "logs")
TESTDATA_PATH = os.path.join(BASE_DIR, "testdata")
TEST_DATA_FILE = os.path.join(TESTDATA_PATH, "test_data.json")

# Default timeouts
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))

# Test metadata
APP_NAME = os.getenv("APP_NAME", "Movie Mobile App")
APP_VERSION = os.getenv("APP_VERSION", "1.0")

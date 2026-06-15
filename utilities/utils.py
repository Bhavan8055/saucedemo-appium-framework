import os
from datetime import datetime
from config.config import SCREENSHOT_PATH


def save_screenshot(driver, test_name: str) -> str:
    os.makedirs(SCREENSHOT_PATH, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_PATH, filename)
    driver.save_screenshot(filepath)
    return filepath


def normalize_text(text: str) -> str:
    return text.strip().lower() if text else ""

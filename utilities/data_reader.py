import json
from config.config import TEST_DATA_FILE


def load_test_data(section: str):
    """Load test data from JSON and return data for a named section."""
    with open(TEST_DATA_FILE, "r", encoding="utf-8") as file:
        content = json.load(file)
    return content.get(section, [])

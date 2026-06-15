import pytest
from pages.login_page import LoginPage
from utilities.logger import get_logger

@pytest.mark.usefixtures("driver")
class TestUserLogin:
    logger = get_logger("LoginTestSuite")

    # Data-Driven Dataset: (username, password, expected_outcome)
    @pytest.mark.parametrize("username, password, should_succeed", [
        ("bod@example.com", "10203040", True),       # Valid User
        ("alice@example.com", "wrong_pass", False),   # Invalid Password
        ("", "", False)                               # Blank Form submission
    ])
    def test_login_scenarios(self, driver, username, password, should_succeed):
        self.logger.info(f"Executing Data-Driven Login Test: User='{username}' | Expected={should_succeed}")
        login_page = LoginPage(driver)
        
        # Action Flow
        login_page.navigate_to_login_screen()
        login_page.login(username, password)
        
        # Validation Matrix
        actual_result = login_page.is_login_successful()
        assert actual_result == should_succeed, f"Assertion failed for user '{username}'. Expected success: {should_succeed}, but got: {actual_result}"
        
        self.logger.info(f"Scenario for '{username}' completed and matched expectations.")
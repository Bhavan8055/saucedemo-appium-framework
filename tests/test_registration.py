import pytest
from pages.registration_page import RegistrationPage
from utilities.data_reader import load_test_data


@pytest.mark.regression
@pytest.mark.parametrize("data", load_test_data("registration"))
def test_user_registration(driver, data):
    """Verify that a new user can register successfully."""
    registration_page = RegistrationPage(driver)
    registration_page.register(
        data["name"],
        data["email"],
        data["password"],
        data["confirm_password"],
    )

    assert registration_page.is_registration_successful(), "Registration success message must be displayed"

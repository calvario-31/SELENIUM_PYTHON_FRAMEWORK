import pytest

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage


@pytest.mark.regression
@pytest.mark.smoke
class TestLogout:
    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_index()
        login_page.login("standard_user", "secret_sauce")

        top_menu_page = TopMenuPage(self.driver)
        top_menu_page.logout()

        assert login_page.verify_page_is_displayed() is True

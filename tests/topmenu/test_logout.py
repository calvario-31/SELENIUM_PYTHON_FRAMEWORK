import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials


class TestLogout:
    login_page: LoginPage
    top_menu_page: TopMenuPage
    driver: WebDriver

    @allure.title("Test logout")
    @allure.description("Verify the logout functionality")
    @allure.testcase("ksBWkBLx", "Test case")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_logout(self, credentials):
        self.login_page.go_to_index()
        self.login_page.login(credentials["username"], credentials["password"])

        self.top_menu_page.logout()

        assert self.login_page.page_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param

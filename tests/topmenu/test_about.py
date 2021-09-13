import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials, get_sauce_labs_href


class TestAbout:
    driver: WebDriver
    login_page: LoginPage
    top_menu_page: TopMenuPage

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.usefixtures("credentials", "href")
    @allure.title("Test about redirection")
    @allure.description("Verify the about option redirection functionality")
    @allure.testcase("moriaEyr", "Test case")
    @allure.severity(allure.severity_level.NORMAL)
    def test_about(self, credentials, href):
        self.login_page.go_to_index()
        self.login_page.login(credentials.get("username"), credentials.get("password"))

        assert self.top_menu_page.get_href_from_about() == href

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param

    @pytest.fixture(params=get_sauce_labs_href())
    def href(self, request):
        return request.param

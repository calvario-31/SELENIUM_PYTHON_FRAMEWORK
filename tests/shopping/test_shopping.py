import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials, get_shopping_list


class TestShopping:
    login_page: LoginPage
    shopping_page: TopMenuPage
    driver: WebDriver

    @pytest.mark.debug
    @pytest.mark.usefixtures("credentials", "shopping_list")
    def test_shopping(self, credentials, shopping_list):
        print("username: " + credentials.get("username"))
        print("password: " + credentials.get("password"))

        for itemData in shopping_list:
            print(itemData.get("itemName"))
            print(itemData.get("price"))

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param

    @pytest.fixture(params=get_shopping_list())
    def shopping_list(self, request):
        return request.param

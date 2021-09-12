import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.checkout.InformationCheckoutPage import InformationCheckoutPage
from pageobjects.checkout.OverviewCheckoutPage import OverviewCheckoutPage
from pageobjects.checkout.DescriptionCheckoutPage import DescriptionCheckoutPage
from pageobjects.checkout.SuccessShoppingPage import SuccessShoppingPage
from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.shopping.DetailItemPage import DetailItemPage
from pageobjects.shopping.ShoppingPage import ShoppingPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials, get_shopping_list
from utilities.fakedatagen.user_info import get_random_user_info


class TestShopping:
    driver: WebDriver
    login_page: LoginPage
    top_menu_page: TopMenuPage
    shopping_page: ShoppingPage
    detail_item_page: DetailItemPage
    information_checkout_page: InformationCheckoutPage
    description_checkout_page: DescriptionCheckoutPage
    overview_checkout_page: OverviewCheckoutPage
    success_shopping_page: SuccessShoppingPage

    @pytest.mark.regression
    @pytest.mark.usefixtures("credentials", "shopping_list", "user_data")
    def test_shopping(self, credentials, shopping_list, user_data):
        self.login_page.go_to_index()
        self.login_page.login(credentials.get("username"), credentials.get("password"))

        total_sum = 0.0
        for item_to_buy in shopping_list:
            self.shopping_page.go_to_item_detail(item_to_buy.get("itemName"))
            price = self.detail_item_page.add_to_cart()
            assert item_to_buy.get("price") == price
            total_sum += price

        assert self.top_menu_page.get_item_count() == len(shopping_list)

        self.top_menu_page.go_to_checkout()

        self.description_checkout_page.continue_checkout()

        self.information_checkout_page.fill_form(user_data.get("firstname"), user_data.get("lastname"),
                                                 user_data.get("zipcode"))

        assert self.overview_checkout_page.get_total_price() == total_sum

        self.overview_checkout_page.finish_checkout()

        assert self.success_shopping_page.title_is_displayed()

        self.success_shopping_page.back_to_home()

        assert self.shopping_page.title_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)
        self.shopping_page = ShoppingPage(self.driver)
        self.detail_item_page = DetailItemPage(self.driver)
        self.description_checkout_page = DescriptionCheckoutPage(self.driver)
        self.information_checkout_page = InformationCheckoutPage(self.driver)
        self.overview_checkout_page = OverviewCheckoutPage(self.driver)
        self.success_shopping_page = SuccessShoppingPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param

    @pytest.fixture(params=get_shopping_list())
    def shopping_list(self, request):
        return request.param

    @pytest.fixture(params=get_random_user_info())
    def user_data(self, request):
        return request.param

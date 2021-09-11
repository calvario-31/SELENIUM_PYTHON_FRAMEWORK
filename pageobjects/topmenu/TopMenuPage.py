import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class TopMenuPage(Page):
    _burgerMenu = (By.ID, "react-burger-menu-btn")
    _logoutButton = (By.ID, "logout_sidebar_link")
    _aboutButton = (By.ID, "about_sidebar_link")
    _itemCountLabel = (By.CLASS_NAME, "shopping_cart_badge")
    _checkoutButton = (By.ID, "shopping_cart_container")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login out")
    def logout(self):
        self._open_burger_menu()
        log.info("Clicking on logout button")
        self._wait_visibility(self._logoutButton).click()

    @allure.step("Opening the burger menu")
    def _open_burger_menu(self):
        self._wait_page_to_load()
        log.info("Opening the burger menu")
        self._find(self._burgerMenu).click()

    def _wait_page_to_load(self):
        self._wait_visibility(self._burgerMenu)

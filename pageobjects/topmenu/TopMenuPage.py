import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class TopMenuPage(Page):
    _burger_menu = (By.ID, "react-burger-menu-btn")
    _logout_button = (By.ID, "logout_sidebar_link")
    _about_button = (By.ID, "about_sidebar_link")
    _item_count_label = (By.CLASS_NAME, "shopping_cart_badge")
    _checkout_button = (By.ID, "shopping_cart_container")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login out")
    def logout(self):
        self.open_burger_menu()
        log.info("Clicking on logout button")
        self._wait_visibility(self._logout_button).click()

    @allure.step("Opening the burger menu")
    def open_burger_menu(self):
        self._wait_to_load()
        log.info("Opening the burger menu")
        self._find(self._burger_menu).click()

    @allure.step("Getting the item count from the UI")
    def get_item_count(self):
        self._wait_to_load()
        log.info("Getting item count text")
        text = self._find(self._item_count_label).text
        log.debug("Item count test: " + text)
        return int(text)

    @allure.step("Clicking on checkout")
    def go_to_checkout(self):
        self._wait_to_load()
        log.info("Clicking on the checkout button")
        self._find(self._checkout_button).click()

    @allure.step("Getting the href from about button and verifying is enabled")
    def get_href_from_about(self):
        self.open_burger_menu()
        about_element = self._find(self._about_button)
        log.info("Verifying the button is enabled")
        if about_element.is_enabled():
            log.info("The button is enabled, getting the href")
            return about_element.get_attribute("href")
        else:
            log.error("The button is not enabled")
            return None

    def _wait_to_load(self):
        self._wait_visibility(self._burger_menu)




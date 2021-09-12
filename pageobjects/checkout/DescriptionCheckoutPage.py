import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class DescriptionCheckoutPage(Page):
    _checkout_button = (By.ID, "checkout")
    _description_label = (By.CLASS_NAME, "cart_desc_label")

    @allure.step("Click on continue checkout")
    def continue_checkout(self):
        self._wait_to_load()
        log.info("Click on continue checkout")
        self._find(self._checkout_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._description_label)

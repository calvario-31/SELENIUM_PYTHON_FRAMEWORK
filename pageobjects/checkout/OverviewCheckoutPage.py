import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class OverviewCheckoutPage(Page):
    _price_label = (By.CLASS_NAME, "summary_subtotal_label")
    _finish_button = (By.ID, "finish")
    _title = (By.CLASS_NAME, "title")

    @allure.step("Getting the total price from UI")
    def get_total_price(self):
        self._wait_to_load()
        log.info("Getting the total price from UI")
        text = self._find(self._price_label).text
        log.debug("Total price: " + text[13:])
        return float(text[13:])

    @allure.step("Finishing checkout")
    def finish_checkout(self):
        log.info("Finishing checkout")
        self._find(self._finish_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._title)
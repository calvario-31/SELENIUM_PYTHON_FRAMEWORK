import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class ShoppingPage(Page):
    _title = (By.CLASS_NAME, "title")

    @allure.step("Verifying the title is displayed")
    def shopping_page_is_displayed(self):
        log.info("Verifying the title is displayed")
        return self._element_is_displayed(self._title)

    @allure.step("Go to item detail")
    def go_to_item_detail(self, product_name):
        self._wait_to_load()
        xpath_generic = "//div[text()='PRODUCT_NAME']"
        xpath_item_name = xpath_generic.replace("PRODUCT_NAME", product_name)
        log.debug("New xpath = " + xpath_item_name)
        current_item_label = (By.XPATH, xpath_item_name)
        log.info("Going to item detail of " + product_name)
        self._find(current_item_label).click()

    def _wait_to_load(self):
        self._wait_visibility(self._title)

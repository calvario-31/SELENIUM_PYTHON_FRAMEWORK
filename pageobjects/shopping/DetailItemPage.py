import string
from decimal import Decimal

import allure
from selenium.webdriver.common.by import By
import utilities.log_manager as log
from pageobjects.Page import Page


class DetailItemPage(Page):
    _item_price = (By.CLASS_NAME, "inventory_details_price")
    _back_to_products_button = (By.ID, "back-to-products")
    _add_to_cart_button = (By.CSS_SELECTOR, "button[id*='add-to-cart']")

    @allure.step("Adding item to cart")
    def add_to_cart(self):
        self._wait_to_load()
        log.info("Getting the price text from UI")
        text = self._find(self._item_price).text
        price = float(text[1:])
        log.debug("Price: " + str(price))
        log.info("Clicking on add to cart")
        self._find(self._add_to_cart_button).click()
        log.info("Clicking on add to products")
        self._find(self._back_to_products_button).click()
        return price

    def _wait_to_load(self):
        self._wait_visibility(self._back_to_products_button)


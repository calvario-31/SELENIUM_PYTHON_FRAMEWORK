import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class SuccessShoppingPage(Page):
    _success_title = (By.CLASS_NAME, "complete-header")
    _back_to_home_button = (By.ID, "back-to-products")

    @allure.step("Verifying the title is displayed")
    def title_is_displayed(self):
        log.info("Verifying the title is displayed")
        return self._element_is_displayed(self._success_title)

    @allure.step("Clicking on back to home")
    def back_to_home(self):
        log.info("Clicking on back to home")
        self._find(self._back_to_home_button).click()

    def _wait_to_load(self):
        pass

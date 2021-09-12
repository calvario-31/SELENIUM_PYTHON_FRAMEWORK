import allure
from selenium.webdriver.common.by import By

import utilities.log_manager as log
from pageobjects.Page import Page


class InformationCheckoutPage(Page):
    _firstname_input = (By.ID, "first-name")
    _lastname_input = (By.ID, "last-name")
    _zipcode_input = (By.ID, "postal-code")
    _continue_button = (By.ID, "continue")
    _title = (By.CLASS_NAME, "title")

    @allure.step("Filling form with firstname: {1}, lastname: {2}, zipcode: {3}")
    def fill_form(self, firstname, lastname, zipcode):
        self._wait_to_load()
        log.info("Filling firstname: " + firstname)
        self._find(self._firstname_input).send_keys(firstname)
        log.info("Filling lastname: " + lastname)
        self._find(self._lastname_input).send_keys(lastname)
        log.info("Filling zipcode: " + zipcode)
        self._find(self._zipcode_input).send_keys(zipcode)
        log.info("Clicking on continue button")
        self._find(self._continue_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._title)

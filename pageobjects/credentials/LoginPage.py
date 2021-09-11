import allure
from selenium.webdriver.common.by import By

from pageobjects.Page import Page
import utilities.log_manager as log


class LoginPage(Page):
    _username_input = (By.ID, "user-name")
    _password_input = (By.ID, "password")
    _login_button = (By.ID, "login-button")
    _bot_image = (By.CLASS_NAME, "bot_column")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Going to index")
    def go_to_index(self):
        self._go_to_index()

    @allure.step("Login into the app with username: {1} and password: {2}")
    def login(self, username, password):
        self._wait_page_to_load()
        log.info("Filling username input")
        log.debug("Username: " + username)
        self._find(self._username_input).send_keys(username)
        log.info("Filling password input")
        log.debug("Password: " + password)
        self._find(self._password_input).send_keys(password)
        log.info("Clicking on login")
        self._find(self._login_button).click()

    @allure.step("Verifying the login page is displayed")
    def verify_page_is_displayed(self):
        log.info("Verifying the login page is displayed")
        return self._element_is_visible(self._bot_image)

    def _wait_page_to_load(self):
        self._wait_visibility(self._bot_image)

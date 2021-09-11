import traceback

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    _main_url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self._driver: WebDriver = driver

    def _find(self, locator):
        return self._driver.find_element(*locator)

    def _wait_visibility(self, locator, time_out=5):
        wait: WebDriverWait = WebDriverWait(self._driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    def _element_is_visible(self, locator, time_out=5):
        try:
            self._wait_visibility(locator, time_out)
            return True
        except TimeoutException:
            print(traceback.print_stack())
            return False

    def _go_to_index(self):
        self._driver.get(self._main_url)

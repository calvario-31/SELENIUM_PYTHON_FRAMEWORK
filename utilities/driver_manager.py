import os

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import utilities.log_manager as log


def build_local_driver(browser):
    log.info("Building local driver")
    if browser == "chrome":
        log.info("Starting chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        log.info("Starting firefox")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        log.info("Starting edge")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        log.error("Bad browser name")
        return None

    driver.maximize_window()
    driver.delete_all_cookies()

    return driver


def build_remote_driver(browser, browser_version, operative_system, os_version):
    log.info("Building remote driver")
    browserstack_local = os.environ["BROWSERSTACK_LOCAL"]
    browserstack_local_identifier = os.environ["BROWSERSTACK_LOCAL_IDENTIFIER"]
    build_name = os.environ["BROWSERSTACK_BUILD_NAME"]
    username = os.environ["BROWSERSTACK_USERNAME"]
    access_key = os.environ["BROWSERSTACK_ACCESS_KEY"]

    remote_url = "https://{}:{}@hub-cloud.browserstack.com/wd/hub".format(username, access_key)

    capabilities = {
        'browser': browser,
        'browser_version': browser_version,
        'os': operative_system,
        'os_version': os_version,
        'browserstack.local': browserstack_local,
        'browserstack.localIdentifier': browserstack_local_identifier,
        'build': build_name,
        'browserstack.debug': 'true',
        'browserstack.console': 'info',
        'browserstack.networkLogs': 'true'
    }

    driver = webdriver.Remote(remote_url, desired_capabilities=capabilities)

    driver.maximize_window()
    driver.delete_all_cookies()

    return driver


def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

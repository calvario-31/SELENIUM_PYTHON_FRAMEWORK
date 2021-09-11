import os

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def build_local_driver(browser):
    if browser == "chrome":
        print("Starting chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        print("Starting firefox")
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser == "edge":
        print("Starting edge")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        print("Bad browser name")
        return None

    driver.maximize_window()
    driver.delete_all_cookies()

    return driver


def build_remote_driver():
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    browser = os.environ["SELENIUM_BROWSER"]
    platform = os.environ["SELENIUM_PLATFORM"]
    remote_url = "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(sauce_username, sauce_access_key)

    capabilities = {
        'browserName': browser,
        'browserVersion': 'latest-1',
        'platformName': platform,
        'sauce:options': {
            'screenResolution': '1920x1080',
        }
    }

    print("Starting sauce labs")
    driver = webdriver.Remote(remote_url, desired_capabilities=capabilities)

    driver.maximize_window()
    driver.delete_all_cookies()

    return driver


def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

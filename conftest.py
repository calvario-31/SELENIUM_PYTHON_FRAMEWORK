import os
import string

from _pytest.config import hookimpl
from _pytest.fixtures import fixture
from selenium.webdriver.remote.webdriver import WebDriver

from src.utilities.driver_manager import take_screenshot, build_remote_driver, \
    build_local_driver
import utilities.log_manager

driver: WebDriver
browser: string
run_on_server: bool


@fixture(scope="function", autouse=True)
def manage_driver(request):
    global driver
    if run_on_server:
        driver = build_remote_driver()
    else:
        driver = build_local_driver(browser)
    request.cls.driver = driver
    yield
    driver.quit()


@fixture(scope="session", autouse=True)
def manage_session(request):
    global browser, run_on_server
    browser = request.config.getoption("--browser")
    run_on_server = os.environ.get('JOB_NAME')
    utilities.log_manager.log = utilities.log_manager.get_logger()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    report = (yield).get_result()
    if report.when == "call":
        setattr(item, "report", report)


@fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.report:
        if request.node.report.failed:
            take_screenshot(driver)

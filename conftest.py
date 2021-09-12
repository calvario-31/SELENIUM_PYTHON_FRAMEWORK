import os
import string

from _pytest.config import hookimpl
from _pytest.fixtures import fixture

import utilities.log_manager as log_manager
from utilities.browserstack_scripts import *
from utilities.driver_manager import build_remote_driver, build_local_driver, take_screenshot

driver: WebDriver
browser: string
browser_version: string
operative_system: string
os_version: string
run_on_server: bool
actual_test_name: string


@fixture(scope="function", autouse=True)
def manage_driver(request):
    global driver, actual_test_name

    if run_on_server:
        driver = build_remote_driver(browser, browser_version, operative_system, os_version)
        write_test_name(driver, request.node.name)
    else:
        driver = build_local_driver(browser)

    actual_test_name = request.node.name.partition("[")[0]
    log_manager.start_test(actual_test_name)

    request.cls.driver = driver
    request.instance.init_pages()
    yield
    driver.quit()


@fixture(scope="session", autouse=True)
def manage_session(request):
    global browser, run_on_server, browser_version, os_version, operative_system
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    operative_system = request.config.getoption("--operative_system")
    os_version = request.config.getoption("--os_version")
    run_on_server = os.environ.get("JOB_NAME")
    log_manager.log = log_manager.get_logger()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default="latest")
    parser.addoption("--operative_system", action="store", default="WINDOWS")
    parser.addoption("--os_version", action="store", default="10")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    global driver, run_on_server, actual_test_name
    report = (yield).get_result()
    if report.when == "call":
        setattr(item, "report", report)
        log_manager.end_test(report.outcome.upper())
        if run_on_server:
            if report.outcome == "passed":
                write_test_status_passed(driver)
            elif report.outcome == "skipped":
                write_test_status_skipped(driver)
            elif report.outcome == "failed":
                write_test_status_failed(driver)


@fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.report:
        if request.node.report.failed:
            take_screenshot(driver)

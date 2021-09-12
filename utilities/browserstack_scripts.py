from selenium.webdriver.remote.webdriver import WebDriver


def write_test_name(driver: WebDriver, test_name):
    driver.execute_script("browserstack_executor: {\"action\": \"setSessionName\", \"arguments\": " +
                          "{\"name\":\" " + test_name + " \" }}")


def write_test_status_passed(driver: WebDriver):
    driver.execute_script("browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": " +
                          "{\"status\": \"passed\", \"reason\": \"Test OK\"}}")


def write_test_status_skipped(driver: WebDriver):
    driver.execute_script("browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": " +
                          "{\"status\": \"skipped\", \"reason\": \"Test OK\"}}")


def write_test_status_failed(driver: WebDriver):
    driver.execute_script("browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": " +
                          "{\"status\": \"failed\", \"reason\": \"\"}}")

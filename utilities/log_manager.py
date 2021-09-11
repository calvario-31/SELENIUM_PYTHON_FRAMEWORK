import logging
import sys


log: logging.Logger


def debug(message):
    global log
    log.debug(message)


def info(message):
    global log
    log.info(message)


def error(message):
    global log
    log.error(message)


def start_test(test_name):
    global log
    print("")
    log.info("------------------------------------------------------------------------------------------")
    log.info("Test: " + test_name)
    log.info("------------------------------------------------------------------------------------------")


def end_test(status):
    global log
    log.info("------------------------------------------------------------------------------------------")
    log.info(status)
    log.info("------------------------------------------------------------------------------------------")
    print("")


def get_logger():
    logger = logging.getLogger("LOG")

    formatter = logging.Formatter("%(asctime)s %(levelname)5s [%(name)s] - %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler("./tests/resources/logs/appLog.log", mode='w', delay=False)

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger2 = logging.getLogger("WDM")
    logger2.setLevel(logging.ERROR)

    logger.setLevel(logging.INFO)

    return logger

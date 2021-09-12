import logging
import os
import sys
from pathlib import Path

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
    log.info("-------------------------------------------------------------------------------------")
    log.info("Test: " + test_name)
    log.info("-------------------------------------------------------------------------------------")


def end_test(status):
    global log
    log.info("-------------------------------------------------------------------------------------")
    log.info(status)
    log.info("-------------------------------------------------------------------------------------")
    print("")


def get_logger():
    log_path = Path("resources/logs/appLog.log")

    os.makedirs(os.path.dirname("./resources/logs/appLog.log"), exist_ok=True)

    logger = logging.getLogger("LOG")

    formatter = logging.Formatter("%(asctime)s %(levelname)5s [%(name)s] - %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(log_path, mode='w', delay=False)

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.setLevel(logging.INFO)

    return logger

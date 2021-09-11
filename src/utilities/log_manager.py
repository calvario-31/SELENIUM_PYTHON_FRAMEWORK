import logging
import sys


log: logging.Logger


def debug(message):
    global log
    log.debug(message)


def info(message):
    global log
    log.info(message)


def get_logger():
    logger = logging.getLogger("LOG")

    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] - %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler('../tests/resources/logs/appLog.log', mode='w', delay=False)

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.setLevel(logging.DEBUG)

    return logger

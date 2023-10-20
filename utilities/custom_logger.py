import inspect
import logging


# TODO: Implement the logger to the framework
def CustomLogger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

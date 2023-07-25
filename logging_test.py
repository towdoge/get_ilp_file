import logging
from logging.handlers import TimedRotatingFileHandler
import sys

SPLIT_STR = "\\" if "win" in sys.platform else "/"


def setup_log(log_dir='', log_level=logging.INFO):
    """
    Set up the basics of logging system. We have two logging handlers:
    one to the console and the other to a log file
    :param log_dir:
    :param log_level:
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel(log_level)
    # 清除之前的处理程序
    tmp = [i for i in logger.handlers]
    for handler in tmp:
        logger.removeHandler(handler)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    # 创建文件处理程序
    file_handler = TimedRotatingFileHandler(
        filename=log_dir + SPLIT_STR + 'running_results.log',
        when='midnight', interval=1, backupCount=7)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # 创建控制台处理程序
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # 添加处理程序到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def setup_log_v1(log_dir="", log_level=logging.INFO):
    """
    Set up the basics of logging system. We have two logging handlers:
    one to the console and the other to a log file
    :param log_dir:
    :param log_level:
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel(log_level)
    # 清除之前的处理程序
    tmp = [i for i in logger.handlers]
    for handler in tmp:
        logger.removeHandler(handler)

    # 创建文件处理程序
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        handlers=[
            logging.FileHandler(log_dir + SPLIT_STR + "running_results.log", mode="w"),
            logging.StreamHandler(),
        ],
        level=log_level,
    )

    return logger

setup_log('logs')
# logger.info('for logs')
logging.info('for logs by logging')
setup_log('newlogs')
# logger.info('for newlogs')
logging.info('for newlogs by logging')

# @Author: u14e
# @Time  : 2019/3/6 15:05
# @description: logger
import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_logger(target_file='u.log'):
    target_dir = os.path.join(BASE_DIR, 'logs')
    target_file = os.path.join(target_dir, target_file)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # TimedRotatingFileHandler
    logHandler = TimedRotatingFileHandler(target_file,
                                          when='midnight',
                                          interval=1,
                                          backupCount=0,
                                          encoding='utf-8')
    logHandler.setFormatter(formatter)

    # StreamHandler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(logHandler)
    logger.addHandler(stream_handler)

    return logger

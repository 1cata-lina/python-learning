# -*- coding: utf-8 -*-
"""日志工具：输出到控制台 + 按日期写入 log/ 目录。全局单例 logger。"""
import logging
import os
import time

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(root_path, "log")
if not os.path.exists(log_path):
    os.mkdir(log_path)

_LOGGER_NAME = "api_test"


class Logger:
    def __init__(self):
        self.logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        self.logger = logging.getLogger(_LOGGER_NAME)
        # 防止重复实例化时重复添加 handler，导致日志重复打印
        if self.logger.handlers:
            return
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        file_handler = logging.FileHandler(self.logname, mode="a", encoding="UTF-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console)


logger = Logger().logger

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging,logging.handlers
import time
import os


class Log(object):

    def logs_output(self, level, message):
        # 这个是日志保存本地的路径
        root_dir = os.path.dirname(os.path.dirname(__file__))
        log_path = root_dir + '/' + 'logs'
        # 文件的命名
        logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # 日志输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(logname, 'a', encoding='utf-8')  # 追加模式
        fh.setLevel(logging.INFO)  # 设置保存到文件的日志等级
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # 设置输出到控制台的日志等级
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def debug(self, message):
        self.logs_output('debug', message)

    def info(self, message):
        self.logs_output('info', message)

    def warning(self, message):
        self.logs_output('warning', message)

    def error(self, message):
        self.logs_output('error', message)




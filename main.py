#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from runner.runner import AutoRunner


class Main(object):
    """
    自动化测试方案的唯一执行入口
    """

    @staticmethod
    def run_test():
        """
        静态的执行方法
        static method
        指的是运行的时候，不用实例化Main类
        """
        runner = AutoRunner()
        print("--开始执行--")
        runner.run_test()
        runner.send_email_test()


if __name__ == "__main__":
    Main.run_test()

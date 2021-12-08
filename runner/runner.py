#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os
import time
from common.main_base import send_email_flag
from common.operate_txt_file import OperateTxtFile
from common.send_email import SendEmail


class AutoRunner(object):

    def run_test(self):
        """
        添加运行方法
        :return:
        """
        # 获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cases_path = path + '/cases'
        print(cases_path)
        html_path = path + '/reports/' + now + '_report.html'
        print(html_path)
        pytest.main([cases_path, '--html={}'.format(html_path), '--self-contained-html'])

    def send_email_test(self):
        """
        发送邮件
        :return:
        """
        if send_email_flag:
            config_file = OperateTxtFile()
            sender = config_file.read_row_keyword("config.txt", "sender")
            print("邮件发送者:%s" % sender)
            receivers = config_file.read_row_keyword("config.txt", "receivers").split(",")
            print("邮件接收者:%s" % receivers)
            server = config_file.read_row_keyword("config.txt","server")
            print("邮件服务器地址:%s" % server)
            password = config_file.read_row_keyword("config.txt", "password")
            print("密码:%s" % password)
            SendEmail().send_email(sender=sender, receivers=receivers, server=server,password=password)

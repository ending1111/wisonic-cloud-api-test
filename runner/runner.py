#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import os
import time
from common.send_email import SendEmail
import configparser


class AutoRunner(object):

    def run_test(self):
        """
        添加运行方法
        :return:
        """
        # 获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        path =os.path.dirname(os.path.dirname(__file__))
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
        root_dir = os.path.dirname(os.path.dirname(__file__))
        print(root_dir)
        file = root_dir + '/config/' + 'param_config.ini'
        print(file)
        config = configparser.ConfigParser()
        config.read(file, encoding='UTF-8')
        # 测试地址
        send_email_flag = config.get("email_flag", "send_email_flag")
        if send_email_flag:
            root_dir = os.path.dirname(os.path.dirname(__file__))
            #print(root_dir)
            file = root_dir + '/config/' + 'param_config.ini'
            #print(file)
            config = configparser.ConfigParser()
            config.read(file, encoding='UTF-8')
            sender = config.get("email", "sender")
            #print("邮件发送者:%s" % sender)
            receivers = config.get("email", "receivers").split(",")
            #print("邮件接收者:%s" % receivers)
            server = config.get("email", "server")
            #print("邮件服务器地址:%s" % server)
            password = config.get("email", "password")
            #print("密码:%s" % password)
            SendEmail().send_email(sender=sender, receivers=receivers, server=server,password=password)

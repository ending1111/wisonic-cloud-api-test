#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


class SendEmail(object):

    def new_report(self):
        # # 测试报告路径
        report_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/reports'
        lists = os.listdir(report_file)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime(report_file + "\\" + fn))  # 按时间排序
        file_new = os.path.join(report_file, lists[-1])  # 获取最新的文件保存到file_new
        print(file_new)
        return file_new

    def send_email(self,sender,receivers,server,password):
        # # 测试报告路径
        file_new = self.new_report()
        # 读取HTML文件内容
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        sender = sender
        receivers = receivers
        msg = MIMEMultipart()
        # 添加正文
        msg['From'] = Header("菜鸟1", 'utf-8')
        msg['To'] = Header('菜鸟2', 'utf-8')
        subject = '邮件测试'
        msg['Subject'] = Header(subject, 'utf-8')
        main_body = '<pre><h1>这是接口自动化测试报告，详情请查阅附件！</h1></pre>'  # 正文的内容
        message = MIMEText(main_body, 'html', 'utf-8')
        msg.attach(message)
        # 添加附件
        att = MIMEText(mail_body, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="test_report.html"'
        msg.attach(att)
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(server)
            smtpobj.login(sender, password)
            smtpobj.sendmail(sender, receivers, str(msg))  # message.as_string()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error:无法发送邮件")

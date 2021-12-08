#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pages.login_page import LoginPage
from common.logs import Log
# from cases.test_login import TestLogin
# from common.operate_txt_file import OperateTxtFile


# @pytest.fixture(scope="class", autouse=True)
# def test_login_token():
#     # 调用获取医院信息接口，返回医院id/科室id 给登录接口调用
#
#     txt_operate = OperateTxtFile()
#     login_phone = txt_operate.read_row_keyword("config.txt", "phone")
#     login_password = txt_operate.read_row_keyword("config.txt", "login_password")
#     hospital_info = LoginPage().get_hospital_info(phone=login_phone)
#     hospitalId = hospital_info["data"][0]["hospitalId"]
#     print(hospitalId)
#     departmentId = hospital_info["data"][0]["departmentList"][0]["id"]
#     print(departmentId)
#     # 登录，获取token
#     token = LoginPage().login_token(phone=login_phone, credentials=login_password, hospitalId=hospitalId,
#                                     departmentId=departmentId)
#     print(token)
#     return token


class TestGetRoom(object):
    """登录后获取诊室信息"""

    def setup_class(self):
        self.log = Log()
        self.page = LoginPage()
        # 调用获取医院信息接口，返回医院id/科室id 给登录接口调用
        # self.txt_operate = OperateTxtFile()
        # self.login_phone = self.txt_operate.read_row_keyword("config.txt", "phone")
        # self.login_password = self.txt_operate.read_row_keyword("config.txt", "login_password")
        # self.hospital_info = self.page.get_hospital_info(phone=self.login_phone)
        # self.hospitalId = self.hospital_info["data"][0]["hospitalId"]
        # print(self.hospitalId)
        # self.departmentId = self.hospital_info["data"][0]["departmentList"][0]["id"]
        # print(self.departmentId)
        # # 登录，获取token
        # self.token = self.page.login_token(phone=self.login_phone,credentials=self.login_password,hospitalId=self.hospitalId,departmentId=self.departmentId)

    def test_get_room_01(self, login_token):
        """正常场景测试"""
        result = self.page.login_room(login_token)
        #print(result)
        assert result["status"] == 200
        self.log.info(result)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_get_room.py"])

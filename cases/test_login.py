#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pages.login_page import LoginPage
from common.logs import Log
from cases.test_hospital_info import TestHospitalInfo
from common.operate_txt_file import OperateTxtFile




class TestLogin(object):
    """云PACS登录"""

    def setup_class(self):
        self.log = Log()
        self.page = LoginPage()

    # 返回token
    # case1 = [
    #     ("13416240604","123456")
    # ]

    # @pytest.mark.parametrize('phone,credentials', case1)
    # def test_login_token_01(self):
    #     """
    #     返回token给其他接口调用
    #     :param phone:
    #     :param credentials:
    #     :param hospitalId:
    #     :param departmentId:
    #     :return:
    #     """
    #     # 调用获取医院信息接口，返回医院id/科室id 给登录接口调用
    #     txt_operate = OperateTxtFile()
    #     login_phone = txt_operate.read_row_keyword("config.txt", "phone")
    #     login_password = txt_operate.read_row_keyword("config.txt", "login_password")
    #     hospital_info = self.page.get_hospital_info(phone=login_phone)
    #     hospitalId = hospital_info["data"][0]["hospitalId"]
    #     print(hospitalId)
    #     departmentId = hospital_info["data"][0]["departmentList"][0]["id"]
    #     print(departmentId)
    #     # 登录，获取token
    #     token = self.page.login_token(phone=login_phone,credentials=login_password,hospitalId=hospitalId,departmentId=departmentId)
    #     print(token)
    #     return token

    # 参数正常场景测试
    case1 = [
        ("13416240604","123456","589139699331895296","602935574747287552"),
        ("15692027190", "123456", "589139699331895296", "602935574747287552")
    ]

    @pytest.mark.parametrize('phone,credentials,hospitalId,departmentId', case1)
    def test_login_01(self,phone,credentials,hospitalId,departmentId):
        """
        登录场景测试
        :param phone:
        :param credentials:
        :param hospitalId:
        :param departmentId:
        :return:
        """
        result = self.page.login(phone=phone,credentials=credentials,hospitalId=hospitalId,departmentId=departmentId)
        print(result)
        assert result["status"] == 200
        self.log.info(result)


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])

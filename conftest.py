#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pages.login_page import LoginPage
from common.operate_txt_file import OperateTxtFile


@pytest.fixture(scope="session")
def login_token():
    txt_operate = OperateTxtFile()
    login_phone = txt_operate.read_row_keyword("config.txt", "phone")
    # print(login_phone)
    login_password = txt_operate.read_row_keyword("config.txt", "login_password")
    # 调用获取医院信息接口，返回医院id/科室id 给登录接口调用
    hospital_info = LoginPage().get_hospital_info(phone=login_phone)
    hospitalId = hospital_info["data"][0]["hospitalId"]
    # print(hospitalId)
    departmentId = hospital_info["data"][0]["departmentList"][0]["id"]
    # print(departmentId)
    # 调用登录接口，获取token
    token = LoginPage().login_token(phone=login_phone, credentials=login_password, hospitalId=hospitalId,departmentId=departmentId)
    return token

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from common.base_request import Baserequest
from common.operate_txt_file import OperateTxtFile


class LoginPage(object):

    def get_hospital_info(self,phone):
        """
        通过手机号获取医院id、科室id,给登录接口调用
        :param phone:
        :return:
        """
        request = Baserequest()
        txt_operate = OperateTxtFile()
        test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = test_env + "/api/pacs/login/hospital"
        print(url)
        params = {"phone":phone}
        r = request.get_noNeedToken_params(url=url,params=params)
        result = r.json()
        #print(result)
        return result

    def login(self, phone, credentials, hospitalId, departmentId):
        """
        登录调用
        :param phone:
        :param credentials:
        :param hospitalId:
        :param departmentId:
        :return:
        """
        request = Baserequest()
        txt_operate = OperateTxtFile()
        test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = test_env + "/api/pacs/login/password"
        data = {
            "phone": phone,
            "credentials": credentials,
            "hospitalId": hospitalId,
            "departmentId": departmentId
        }
        r = request.post_noNeedToken(url, data)
        result = r.json()
        return result

    def login_token(self, phone, credentials, hospitalId, departmentId):
        """
        登录成功后返回token，给其他接口调用
        :param phone:
        :param credentials:
        :param hospitalId:
        :param departmentId:
        :return:
        """
        request = Baserequest()
        txt_operate = OperateTxtFile()
        test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = test_env + "/api/pacs/login/password"
        data = {
            "phone": phone,
            "credentials": credentials,
            "hospitalId": hospitalId,
            "departmentId": departmentId
        }
        token = request.post_result_token(url, data)
        return token

    def login_room(self,token):
        """
        登录成功后获取诊室信息
        :param token:
        :return:
        """
        request = Baserequest()
        txt_operate = OperateTxtFile()
        test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = test_env + "/api/pacs/login/room"
        r = request.get(url,token)
        result = r.json()
        return result


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from common.base_request import Baserequest
from common.operate_txt_file import OperateTxtFile
import configparser
import os


class LoginPage(object):

    root_dir = os.path.dirname(os.path.dirname(__file__))
    print(root_dir)
    file = root_dir + '/config/' + 'param_config.ini'
    print(file)
    config = configparser.ConfigParser()
    config.read(file, encoding='UTF-8')
    # 测试地址
    test_env = config.get("env","test_env")
    print(test_env)
    request = Baserequest()

    def get_hospital_info(self,phone):
        """
        通过手机号获取医院id、科室id,给登录接口调用
        :param phone:
        :return:
        """
        # request = Baserequest()
        # txt_operate = OperateTxtFile()
        # test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = self.test_env + "/api/pacs/login/hospital"
        print(url)
        params = {"phone":phone}
        r = self.request.get_noNeedToken_params(url=url,params=params)
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
        # request = Baserequest()
        # txt_operate = OperateTxtFile()
        # test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = self.test_env + "/api/pacs/login/password"
        data = {
            "phone": phone,
            "credentials": credentials,
            "hospitalId": hospitalId,
            "departmentId": departmentId
        }
        r = self.request.post_noNeedToken(url, data)
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
        # request = Baserequest()
        # txt_operate = OperateTxtFile()
        # test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = self.test_env + "/api/pacs/login/password"
        data = {
            "phone": phone,
            "credentials": credentials,
            "hospitalId": hospitalId,
            "departmentId": departmentId
        }
        token = self.request.post_result_token(url, data)
        return token

    def login_room(self,token):
        """
        登录成功后获取诊室信息
        :param token:
        :return:
        """
        # request = Baserequest()
        # txt_operate = OperateTxtFile()
        # test_env = txt_operate.read_row_keyword("config.txt", "test_env")
        url = self.test_env + "/api/pacs/login/room"
        r = self.request.get(url,token)
        result = r.json()
        return result


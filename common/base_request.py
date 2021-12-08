#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Baserequest(object):

    def post_noNeedToken(self, url, data):
        """
        给不需要token的接口调用
        :param url:
        :param data:
        :return:
        """
        headers = {
            "Content-Type": "application/json",
        }
        return requests.post(url, json=data, headers=headers)

    def post(self, url, data, token):
        """
        给需要token的接口调用
        :param url:
        :param data:
        :return:
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        return requests.post(url, json=data, headers=headers)

    def post_result_token(self, url, data):
        """
        给登录接口调用，返回token
        :param url:
        :param data:
        :return:
        """
        requests = Baserequest()
        r = requests.post_noNeedToken(url, data)
        result = r.json()
        if result["status"] == 200:
            Authorization = "Bearer" + " " + result["data"]["accessToken"]
            return Authorization
        else:
            print(result)

    def get_params(self, url, token, params):
        """
        接口带参数
        给需要token的接口调用
        :param url:
        :return:
        """
        header = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        return requests.get(url, headers=header,params=params)

    def get(self, url, token):
        """
        接口不带参数
        给需要token的接口调用
        :param url:
        :return:
        """
        header = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        return requests.get(url, headers=header)

    def get_noNeedToken(self, url):
        """
        接口不带参数
        给不需要token的接口调用
        :param url:
        :return:
        """
        header = {
            "Content-Type": "application/json",
        }
        return requests.get(url, headers=header)

    def get_noNeedToken_params(self, url,params):
        """
        接口带参数
        给不需要token的接口调用
        :param url:
        :return:
        """
        header = {
            "Content-Type": "application/json",
        }
        return requests.get(url, headers=header,params=params)
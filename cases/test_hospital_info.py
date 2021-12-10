#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pages.login_page import LoginPage
from common.logs import Log


class TestHospitalInfo(object):
    """登录前通过手机号码获取医院信息"""

    def setup_class(self):
        self.log = Log()
        self.page = LoginPage()

    # 参数正常场景测试
    case1 = [
        ("13416240604"),
        ("15692027190")
    ]

    @pytest.mark.parametrize('phone', case1)
    def test_get_hospital_info_01(self, phone):
        """
        参数正常场景测试
        :param phone:
        :return:
        """
        result = self.page.get_hospital_info(phone=phone)
        print(result)
        assert result["status"] == 200
        self.log.info(result)





if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_hospital_info.py"])

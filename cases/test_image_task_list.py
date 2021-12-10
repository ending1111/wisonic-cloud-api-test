#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pages.image_quality_page import ImageQualityPage
from common.logs import Log
from common.main_base import pro_env


class TestImageTaskList(object):
    """图像质检任务列表接口测试：/api/uniqc/image-qc/task-list"""

    def setup_class(self):
        self.log = Log()
        self.page = ImageQualityPage()


    # 参数正常场景测试
    case1 = [
        (1, 10, "2021-11")
    ]

    @pytest.mark.parametrize('pageNumber,pageSize,months', case1)
    def test_image_task_list_01(self, pageNumber, pageSize, months):
        """
        传参正确，列表数据获取成功
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        # print(reslut)
        assert result["status"] == 200
        self.log.info(result)

    # 参数不全场景测试
    # pageSize为空，默认10
    # months为空，默认查全部
    case2 = [
        (None, 10, "2021-11"),
        (1, None, "2021-11"),
        (1, 12, None)
    ]

    @pytest.mark.parametrize('pageNumber,pageSize,months', case2)
    def test_image_task_list_02(self, pageNumber, pageSize, months):
        """
        参数不全
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        # print(reslut)
        assert result["status"] == 200
        self.log.info(result)

    # pageNumber参数值异常场景测试
    case3 = [
        (-1, 10, "2021-11"),
        (0, 10, "2021-11")
    ]

    @pytest.mark.skipif(condition=pro_env,reason="跳过该测试用例")
    @pytest.mark.parametrize('pageNumber,pageSize,months', case3)
    def test_image_task_list_03(self, pageNumber, pageSize, months):
        """
        pageNumber参数值异常
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        assert result["status"] == 5003
        self.log.info(result)

    # pageNumber参数异常场景测试
    # pageNumber赋值0.5
    case4 = [(0.5, 10, "2021-11")]

    @pytest.mark.parametrize('pageNumber,pageSize,months', case4)
    def test_image_task_list_04(self, pageNumber, pageSize, months):
        """
        pageNumber参数值异常
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        assert result["status"] == 1004
        self.log.info(result)

    # pageSize参数值异常场景测试
    case5 = [
        (-1, 10, "2021-11"),
        (0, 10, "2021-11")
    ]

    @pytest.mark.parametrize('pageNumber,pageSize,months', case5)
    def test_image_task_list_05(self, pageNumber, pageSize, months):
        """
        pageSize参数值异常
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        assert result["status"] == 5003
        self.log.info(result)

    # months参数异常场景
    case6 = [
        (1, 10, "测试"),
        (1, 10, "202111"),
        (1, 10, 202111)
    ]

    @pytest.mark.parametrize('pageNumber,pageSize,months', case6)
    def test_image_task_list_06(self, pageNumber, pageSize, months):
        """
        months参数值异常
        :return:
        """
        result = self.page.image_task_list(pageNumber=pageNumber, pageSize=pageSize, months=months)
        assert result["status"] == 3002
        self.log.info(result)


if __name__ == '__main__':
    pytest.main(["-v","-s", "test_image_task_list.py"])

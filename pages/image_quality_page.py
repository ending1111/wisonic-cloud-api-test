#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from common.base_request import Baserequest
from common.operate_txt_file import OperateTxtFile
import configparser
import os

class ImageQualityPage(object):

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

    def image_task_list(self,pageNumber,pageSize,months):
        """
        图像质检任务列表
        :param pageNumber:
        :param pageSize:
        :param months:
        :return:
        """
        # request = Baserequest()
        # txt_operate = OperateTxtFile()
        # test_env = txt_operate.read_row_keyword("config.txt","test_env")
        params = {"pageNumber":pageNumber,"pageSize":pageSize,"months":months}
        url = self.test_env + "/api/uniqc/image-qc/task-list"
        r = self.request.get_noNeedToken_params(url=url,params=params)
        result = r.json()
        #print(result)
        return result
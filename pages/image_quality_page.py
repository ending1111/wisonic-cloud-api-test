#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from common.base_request import Baserequest
from common.operate_txt_file import OperateTxtFile

class ImageQualityPage(object):

    def image_task_list(self,pageNumber,pageSize,months):
        """
        图像质检任务列表
        :param pageNumber:
        :param pageSize:
        :param months:
        :return:
        """
        request = Baserequest()
        txt_operate = OperateTxtFile()
        test_env = txt_operate.read_row_keyword("config.txt","test_env")
        params = {"pageNumber":pageNumber,"pageSize":pageSize,"months":months}
        url = test_env + "/api/uniqc/image-qc/task-list"
        r = request.get_noNeedToken_params(url=url,params=params)
        result = r.json()
        #print(result)
        return result
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re


class OperateTxtFile(object):

    def read_rows(self, file):
        """
        读取多行文件,返回所有
        :param file:
        :return:
        """
        f = open(file, "r",encoding="utf-8")
        line = f.readlines()
        array =[]
        for i in line:
            array.append(i.strip("\n"))
        f.close()
        return array

    def read_row(self,file,keyword):
        """
        读取文件，返回与keyword匹配的单行数据
        :return:
        """
        data = ""
        f = open(file, "r", encoding="utf-8")
        line = f.readlines()
        array = []
        for i in line:
            i = i.strip("\n")
            pattern = re.search("#",i)
            if len(i) == 0 or pattern:
                # print(i)
                pass
            else:
                # print(i)
                array.append(i)
        for line in array:
            if re.search(keyword, line):
                # print(line)
                pattern = re.compile('"(.*)"')
                data = pattern.findall(line)[0]
        if data == "":
            print("没有找到关键字匹配数据")
        f.close()
        return data

    def read_row_keyword(self,file,keyword):
        """
        读取txt文件中的keyword对应的信息
        :param file:
        :param keyword:
        :return:
        """
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/datas/%s" % file
        print(file_path)
        line = self.read_row(file_path, keyword)
        #print(line)
        return line

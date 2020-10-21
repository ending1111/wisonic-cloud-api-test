# 测试用例仓库使用说明

## 项目文件结构
```
project
├──api                #api数据
├──data               #参数化数据驱动数据集
├──reports            #运行测试用例后生成的
├──testcases          #测试用例
├──testsuites         #测试用例集合
├──.env               #本地环境配置
├──.test-env          #自动化测试环境配置
├──debugtalk.py       #逻辑运算辅助函数
├──requirements.txt   #项目依赖
```

## 编写测试用例
   todo

## 执行测试用例
   安装依赖
   ```shell script
   pip install -r requirements.txt
   ```
   执行测试
   ```shell script
   hrun testcase_paths
   ```

## 自定义校验器
   编写完自定义的校验器后，如果校验器引入了其他依赖，需更新```requirements.txt```

## Jenkins集成
todo

## 从Yapi导入api接口数据
1.  打开[Yapi](http://192.168.1.207:3000/) 进入项目列表，选择项目，点击数据管理。在数据导出中以json格式导出全部接口

2.  使用```yapi2hrun```工具将Yapi导出的api.json转换成hrun的api文件（[yapi2hrun项目安装](http://192.168.1.208:8929/wisonic-cloud/yapi2hrun) ）
    ```shell script
    yapi2hrun api.json
    ```
    执行成功后，将在执行目录下生成api文件夹


## 参考
1. 目前项目使用的版本是2.5.7，请参考V2版本说明：[HttprunnerDoc_V2.x](https://v2.httprunner.org/)

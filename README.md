# 测试用例仓库使用说明

## 参考文档
1. [Httprunner](https://cn.httprunner.org/)

## 从Yapi导入api接口数据
1.  打开[Yapi](http://192.168.1.207:3000/) 进入项目列表，选择项目，点击数据管理。在数据导出中以json格式导出全部接口

2.  使用```yapi2hrun```工具将Yapi导出的api.json转换成hrun的api文件（[yapi2hrun项目安装](http://192.168.1.208:8929/wisonic-cloud/yapi2hrun) ）
    ```shell script
    yapi2hrun api.json
    ```
    执行成功后，将在执行目录下生成api文件夹

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
   如果是venv环境，运行命令
   ```shell script
   pip freeze > requirements.txt
   ```
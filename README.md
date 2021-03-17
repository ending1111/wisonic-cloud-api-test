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

## 基本概念
在 HttpRunner 中，测试用例组织主要基于三个概念：

- 测试用例集（testsuite）：对应一个文件夹，包含单个或多个测试用例（`YAML/JSON`）文件
- 测试用例（testcase）：对应一个 `YAML/JSON` 文件，包含单个或多个测试步骤
- 测试步骤（teststep）：对应 `YAML/JSON` 文件中的一个 `test`，描述单次接口测试的全部内容，包括发起接口请求、解析响应结果、校验结果等

## 编写测试用例
```yaml
- config:
    name: 设备账号登录
    base_url: ${ENV(base_url)}

- test:
    name: 登录国内账号
    api: api/设备API/账号登录.yaml
    variables:
        userName: 13333333333
        password: 123456

- test:
    name: 账号不存在
    api: api/设备API/账号登录.yaml
    variables:
        userName: 644639584
        password: 123456
        validate:
    validate:
      - eq: [content.responseHeader.errorInfo, the doctor user is not exist]

- test:
    name: 密码错误
    api: api/设备API/账号登录.yaml
    variables:
        userName: 644639583
        password: 111111
    validate:
      - eq: [content.responseHeader.errorInfo, Input password is wrong]
```

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
HttpRunner基于Python开发，理论上可以使用任何Py库。扩展自定义的校验规则时，可以扩展```debugtalk.py```来实现自己的需求。

下面是自定义json schema校验的样例。

```python
# -*- coding: UTF-8 -*-
from jsonschema import validate
from jsonschema import ValidationError
from httprunner.exceptions import ValidationFailure

def json_schema(json, schema):
    try:
        validate(instance=json, schema=schema)
    except ValidationError as e:
        raise ValidationFailure("Bad json") from e
```
   编写完自定义的校验器后，如果校验器引入了其他依赖，需更新```requirements.txt```

## Jenkins集成
在Jenkins中可设置自动进行测试用例的执行，并将测试结果通知到企业微信

```sh
#!/bin/bash -l
pip3 install -r requirements.txt
result=$?
hrun testcases --dot-env-path .test-env --report-file reports/report-${BUILD_NUMBER}.html
echo 测试报告地址 ${JOB_URL}ws/reports/report-${BUILD_NUMBER}.html
grep -q "<th class=\"error\" style=\"width:5em;\">\|<th class=\"failure\" style=\"width:5em;\">" reports/report-${BUILD_NUMBER}.html && exit 1
```

其中，脚本第5行用于判断测试报告中用例是否全部成功，若有失败则将Jenkins构建结果设为失败。

## 从Yapi导入api接口数据
1.  打开[Yapi](http://192.168.1.207:3000/) 进入项目列表，选择项目，点击数据管理。在数据导出中以json格式导出全部接口

2.  使用```yapi2hrun```工具将Yapi导出的api.json转换成hrun的api文件（[yapi2hrun项目安装](http://192.168.1.208:8929/wisonic-cloud/yapi2hrun) ）
    ```shell script
    yapi2hrun api.json
    ```
    执行成功后，将在执行目录下生成api文件夹


## 参考
1. 目前项目使用的版本是2.5.7，请参考V2版本说明：[HttprunnerDoc_V2.x](https://v2.httprunner.org/)

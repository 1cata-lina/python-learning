# -*- coding: utf-8 -*-
"""数据驱动引擎：读取 YAML 用例 -> 发请求 -> 提取变量 -> 断言。

YAML 用例格式（data/*_center.yaml）：
  case_name:
    - request_info:          # 接口基本信息
        case_title: 用例标题   # 会写入 allure 报告
        url: /posts/1
        method: GET
        headers: {...}
      case_info:              # 用例列表，可多条
        - json: {...}         # 请求体（data / params / json 均可）
          extract:            # 可选：从响应提取变量写入 extract.yaml
            post_id: $.id
          validate:           # 可选：断言列表
            - eq: [ '$.id', 1 ]
"""
import allure

from core.http_client import RestClient
from utils.assert_util import AssertUtil
from utils.extract_util import ExtractUtil


class ApiService:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtil()

    def handle_case(self, test_data, login_token=None):
        request_info = test_data['request_info']
        # 1. 解析请求基本信息（url 支持 ${} 变量引用）
        url = self.extract.extract_url(request_info['url'])
        method = request_info['method']
        headers = request_info.get('headers') or {}
        if login_token:
            headers.update(login_token)

        # 2. 动态标题写入 allure 报告
        allure.dynamic.title(request_info.get('case_title', '未命名用例'))

        # 3. 拆分断言 / 提取规则，剩余为请求参数
        case_info = test_data['case_info']
        validate = case_info.pop("validate", None)
        extract = case_info.pop("extract", None)
        case_info = self.extract.extract_case(case_info)

        # 4. 发送请求
        res = self.session.do_request(url=url, method=method, headers=headers, **case_info)

        # 5. 按 extract 规则提取变量写入 extract.yaml
        self.extract.extract_data(res, extract)

        # 6. 按 validate 规则断言
        if validate:
            AssertUtil().validate_response(res, validate)
        return res

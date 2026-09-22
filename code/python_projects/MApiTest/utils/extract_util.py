# -*- coding: utf-8 -*-
"""提取工具：
1. 把接口返回的变量（如 token、id）写入 extract.yaml，供后续用例复用；
2. 解析用例中的 ${函数(参数)} 动态表达式，如 ${get_time()} / ${get_extract_value(post_id)}。
"""
import json
import random
import time

from utils.assert_util import AssertUtil
from utils.log_util import logger
from utils.yaml_util import YamlUtil


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extract_data(self, res, extract):
        """按 extract 规则（如 {post_id: '$.id'}）从响应中取值并写入 extract.yaml"""
        if not extract:
            return
        for key, expression in extract.items():
            try:
                value = self.jsonpath_util.extract_by_jsonpath(res, expression)
                self.yaml_util.write_extra_yaml({key: value})
            except Exception as e:
                logger.error("变量{}写入extract.yaml失败，请检查，error={}".format(key, e))

    def get_extract_value(self, key):
        """从 extract.yaml 读取之前提取的变量"""
        try:
            data = self.yaml_util.read_extract_yaml()
            if not data:
                raise KeyError("extract.yaml 为空")
            return data[key]
        except Exception as e:
            logger.error("从yaml中根据{}获取不到内容，error={}".format(key, e))
            return None

    def extract_url(self, url):
        """URL 支持 ${} 变量引用，如 /posts/${get_extract_value(post_id)}"""
        if "${" in url and "}" in url:
            return self.process_data(url)
        return url

    def process_data(self, data):
        """解析字符串中的 ${函数(参数)}，循环处理直到没有表达式为止"""
        while "${" in data and "}" in data:
            start_index = data.index("$")
            end_index = data.index("}")
            func_full_name = data[start_index: end_index + 1]
            func_name = data[start_index + 2: data.index("(")]
            func_params = data[data.index("(") + 1: data.index(")")]
            func = getattr(self, func_name, None)
            if func is None:
                logger.warning("未找到动态函数: {}".format(func_name))
                data = data.replace(func_full_name, "None")
                continue
            params = func_params.split(",") if func_params else []
            params = [int(p) if p.isdigit() else p for p in params]
            result = func(*params)
            data = data.replace(func_full_name, str(result))
        return data

    def extract_case(self, case_info):
        """把用例参数整体转字符串 -> 替换 ${} 表达式 -> 转回 dict"""
        str_case_info = json.dumps(case_info)
        data = self.process_data(str_case_info)
        return json.loads(data)

    # ---- 内置动态函数 ----
    def get_time(self):
        return int(time.time())

    def get_random(self, num1, num2):
        return random.randint(int(num1), int(num2))

    def get_add(self, num1, num2):
        return int(num1) + int(num2)

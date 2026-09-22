# -*- coding: utf-8 -*-
"""底层 HTTP 客户端：只负责发请求 + 记录请求/响应日志，不关心业务。

使用方法：
    client = RestClient()
    client.get("/posts", params=...)   # 返回 requests.Response
    client.do_request("/posts", "POST", json={...})  # 返回解析后的 dict
"""
import json

import requests

from utils.file_reader import base_data
from utils.log_util import logger

api_root_url = base_data.read_ini()['host']['api_sit_url']


class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url
        self.session = requests.Session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, "POST", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "PUT", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        full_url = self.api_root_url + url
        if method == "GET":
            return self.session.get(full_url, **kwargs)
        if method == "POST":
            return self.session.post(full_url, **kwargs)
        if method == "PUT":
            return self.session.put(full_url, **kwargs)
        if method == "DELETE":
            return self.session.delete(full_url, **kwargs)
        raise ValueError("不支持的请求方法: {}".format(method))

    def do_request(self, url, method, **kwargs):
        """发送请求并直接返回解析后的 JSON（供数据驱动引擎使用）"""
        response = self.request(url, method, **kwargs)
        try:
            return response.json()
        except ValueError:
            logger.warning("响应不是 JSON，已返回原文文本")
            return response.text

    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(self.api_root_url + url))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
        if headers is not None:
            logger.info("接口请求的headers参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))

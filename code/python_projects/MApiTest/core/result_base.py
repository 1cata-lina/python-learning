# -*- coding: utf-8 -*-
"""统一响应结果类：process_response 解析后的标准返回对象"""


class ResultResponse:
    def __init__(self):
        self.success = False
        self.body = None
        self.status_code = None

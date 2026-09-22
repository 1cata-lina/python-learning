# -*- coding: utf-8 -*-
"""响应处理工具：把 requests.Response 统一转换为 ResultResponse。"""
import json

from core.result_base import ResultResponse
from utils.log_util import logger


def process_response(response):
    """把响应解析为 ResultResponse(success/body/status_code)"""
    result = ResultResponse()
    result.status_code = response.status_code
    if response.status_code in (200, 201, 202, 204):
        result.success = True
        try:
            result.body = response.json()
        except ValueError:
            result.body = response.text
    else:
        result.success = False
        logger.info("接口状态码不是2开头，请检查: {}".format(response.status_code))
    try:
        logger.info("接口的返回内容>>>：" + json.dumps(result.body, ensure_ascii=False))
    except (TypeError, ValueError):
        logger.info("接口的返回内容>>>：{}".format(result.body))
    return result

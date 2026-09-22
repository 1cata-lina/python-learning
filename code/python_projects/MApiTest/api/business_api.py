# -*- coding: utf-8 -*-
"""业务接口层：组装请求参数、处理返回结果，供手写模式用例调用。

示例基于 jsonplaceholder Posts 资源；换成自己的项目时改写函数体即可。
"""
from core.api_factory import api_util
from utils.response_util import process_response


def get_posts(params=None):
    """获取帖子列表"""
    response = api_util.get_posts(params=params)
    return process_response(response)


def get_post(post_id):
    """获取帖子详情"""
    response = api_util.get_post(post_id)
    return process_response(response)


def create_post(json_data):
    """创建帖子"""
    response = api_util.create_post(json=json_data)
    return process_response(response)


def update_post(post_id, json_data):
    """更新帖子"""
    response = api_util.update_post(post_id, json=json_data)
    return process_response(response)


def delete_post(post_id):
    """删除帖子"""
    response = api_util.delete_post(post_id=post_id)
    return process_response(response)

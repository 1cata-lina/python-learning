# -*- coding: utf-8 -*-
"""接口方法层：把 HTTP 接口封装成 Python 方法，按业务模块扩展。

示例基于公共测试接口 https://jsonplaceholder.typicode.com（Posts 资源）。
换成自己的项目时，只需新增方法并指向对应 url 即可。
"""
from core.http_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    # ---- Posts 资源（jsonplaceholder 示例）----
    def get_posts(self, **kwargs):
        return self.get("/posts", **kwargs)

    def get_post(self, post_id, **kwargs):
        return self.get("/posts/{}".format(post_id), **kwargs)

    def create_post(self, **kwargs):
        return self.post("/posts", **kwargs)

    def update_post(self, post_id, **kwargs):
        return self.put("/posts/{}".format(post_id), **kwargs)

    def delete_post(self, **kwargs):
        return self.delete("/posts/{}".format(kwargs.pop("post_id")), **kwargs)


api_util = Api()

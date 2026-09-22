# -*- coding: utf-8 -*-
"""传统手写模式示例：api 层封装 + 直接断言。两种模式可并存，任选其一即可。"""
import allure

from api.business_api import create_post, get_post, get_posts


@allure.feature("Posts 模块（手写模式）")
class TestPostsManual:
    @allure.story("查询")
    @allure.title("获取帖子列表")
    def test_get_posts(self):
        result = get_posts()
        assert result.success is True
        assert result.status_code == 200
        assert len(result.body) >= 1

    @allure.title("获取帖子详情")
    def test_get_post(self):
        result = get_post(1)
        assert result.success is True
        assert result.body["id"] == 1

    @allure.title("创建帖子")
    def test_create_post(self):
        result = create_post({"title": "foo", "body": "bar", "userId": 1})
        assert result.success is True
        assert result.body["title"] == "foo"

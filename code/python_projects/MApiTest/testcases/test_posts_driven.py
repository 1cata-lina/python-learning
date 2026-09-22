# -*- coding: utf-8 -*-
"""数据驱动模式示例：用例定义在 data/posts_center.yaml，改 yaml 即可加用例，无需写代码。"""
import allure
import pytest

from core.api_service import ApiService
from utils.yaml_util import YamlUtil


@allure.feature("Posts 模块（数据驱动）")
class TestPostsDriven:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("posts_center.yaml", "get_post"))
    def test_get_post(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case("posts_center.yaml", "list_posts"))
    def test_list_posts(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case("posts_center.yaml", "create_post"))
    def test_create_post(self, data):
        ApiService().handle_case(data)

    @pytest.mark.parametrize("data", YamlUtil().extract_case("posts_center.yaml", "update_post"))
    def test_update_post(self, data):
        ApiService().handle_case(data)

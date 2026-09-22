# -*- coding: utf-8 -*-
"""YAML 工具：读取用例 yaml、读写 extract.yaml（跨用例变量共享）。"""
import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")

    def _full_path(self, yaml_name):
        return os.path.join(self.data_path, yaml_name)

    def read_extract_yaml(self):
        """读取 extract.yaml，不存在或为空返回 None"""
        path = self._full_path("extract.yaml")
        if not os.path.exists(path):
            return None
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def read_testcases_yaml(self, yaml_name, key_name=None):
        """读取用例 yaml，可按 key 取值"""
        with open(self._full_path(yaml_name), encoding="utf-8") as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

    def extract_case(self, yaml_name, key_name):
        """把 yaml 用例转换为 ApiService 可用的 case 列表。

        yaml 结构：
          case_name:
            - request_info: {...}
              case_info: [ {...}, {...} ]
        """
        case_value = self.read_testcases_yaml(yaml_name, key_name)[0]
        new_case = []
        for value in case_value["case_info"]:
            new_case.append({
                "request_info": case_value["request_info"],
                "case_info": value,
            })
        return new_case

    def write_extra_yaml(self, data):
        """把提取的变量写入 extract.yaml（与旧值合并后覆盖写入）"""
        old_value = self.read_extract_yaml()
        if old_value is None:
            old_value = {}
        for key, value in data.items():
            old_value[key] = value
        with open(self._full_path("extract.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(old_value, stream=f, allow_unicode=True, sort_keys=False)

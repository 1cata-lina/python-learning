# -*- coding: utf-8 -*-
"""配置文件/数据文件读取工具。

统一从 config/settings.ini 读环境配置，从 data/ 下读 yaml 数据。
"""
import configparser
import os

import yaml


class FileReader:
    def __init__(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.ini_path = os.path.join(root_dir, "config", "settings.ini")
        self.data_path = os.path.join(root_dir, "data", "data.yaml")
        self.file_path = os.path.join(root_dir, "file", "upload.jpeg")

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding="utf-8")
        return config

    def read_data(self):
        with open(self.data_path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def read_file(self):
        """读取上传文件，返回 requests 可用的 files 参数"""
        file = open(self.file_path, "rb")
        return {"file": ("upload.jpeg", file, "image/jpeg")}


base_data = FileReader()

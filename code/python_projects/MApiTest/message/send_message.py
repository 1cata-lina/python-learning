# -*- coding: utf-8 -*-
"""消息推送：把测试结果推送到钉钉/企业微信群机器人。

用法：
    1. 在钉钉/企微群里添加"自定义机器人"，拿到 webhook 地址
    2. 填入下方 WEBHOOK，或运行时传入
    3. 手动执行：python -m message.send_message
       （不会在 import 时自动发送，避免误触发）
"""
import requests

WEBHOOK = ""  # TODO 填入你的群机器人 webhook


def push_message(content, webhook=WEBHOOK):
    if not webhook:
        raise ValueError("请先在 message/send_message.py 中配置 webhook 地址")
    payload = {
        "msgtype": "text",
        "text": {"content": content},
    }
    resp = requests.post(url=webhook, json=payload, timeout=10)
    resp.raise_for_status()


if __name__ == "__main__":
    push_message("接口自动化测试执行完成")

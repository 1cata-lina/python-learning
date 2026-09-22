# -*- coding: utf-8 -*-
"""全局 fixture"""
import pytest

from utils.log_util import logger


@pytest.fixture(scope="session", autouse=True)
def session_log():
    logger.info("=== 测试会话开始 ===")
    yield
    logger.info("=== 测试会话结束 ===")

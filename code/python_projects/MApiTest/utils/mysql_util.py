# -*- coding: utf-8 -*-
"""MySQL 工具：惰性连接，需要时再连库，用于测试后校验数据库数据。

使用前先在 config/settings.ini 的 [mysql] 段填入自己的连接信息；
host 为空时不会发起连接，相关用例会跳过数据库校验。
"""
import pymysql

from utils.file_reader import base_data
from utils.log_util import logger

data = base_data.read_ini()['mysql']
DB_CONF = {
    "host": data.get('MYSQL_HOST', ''),
    "port": int(data.get('MYSQL_PORT', 3306) or 3306),
    "user": data.get('MYSQL_USER', ''),
    "password": data.get('MYSQL_PASSWD', ''),
    "db": data.get('MYSQL_DB', ''),
}


class MysqlDb:
    def __init__(self):
        if not DB_CONF["host"]:
            raise ValueError("未配置 MySQL 连接信息，请在 config/settings.ini 的 [mysql] 段填写")
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception:
            pass

    def select_db_one(self, sql):
        logger.info("执行sql：{}".format(sql))
        self.cur.execute(sql)
        result = self.cur.fetchone()
        logger.info("sql执行结果：{}".format(result))
        return result

    def select_db_all(self, sql):
        logger.info("执行sql：{}".format(sql))
        self.cur.execute(sql)
        result = self.cur.fetchall()
        logger.info("sql执行结果：{}".format(result))
        return result

    def execute_db(self, sql):
        try:
            logger.info("执行sql：{}".format(sql))
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


def get_db():
    """获取数据库连接；未配置时返回 None 并提示"""
    if not DB_CONF["host"]:
        logger.warning("未配置 MySQL，跳过数据库操作")
        return None
    return MysqlDb()

'''Python
csv模块（内置模块，无需pip安装）

csv模块用来读写csv逗号分隔文本文件，测试中常用于保存测试数据、日志、用例数据。

一、核心类与方法
表格
方法 / 类
作用
csv.reader()
按行读取csv，返回列表，无表头映射
csv.DictReader()
读取，自动把第一行作为表头，返回字典
csv.writer()
写入，按列表写入一行
csv.DictWriter()
字典写入，需要指定表头字段

编码重点：Windows打开csv容易乱码，写文件建议
encoding = "utf-8-sig"

二、读取文件（reader）'''
import csv

with open("test.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    # 跳过表头，next只执行一次
    header = next(reader)
    print("表头：", header)
    for row in reader:
        print(row)  # row 是列表
#
# 三、DictReader（字典读取，最常用）

import csv

with open("test.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 通过表头字段取值
        print(row["id"], row["case_name"])

'''四、写入
writer（列表写入）'''

import csv

data = [
    ["id", "case_name", "result"],
    [1, "登录正常", "pass"],
    [2, "密码错误", "fail"]
]

with open("result.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

'''newline = ""
必须加：防止Windows写入多出空行。

五、DictWriter（字典写入，项目高频）
'''
import csv

fields = ["id", "case_name", "result"]
rows = [
    {"id": 1, "case_name": "登录正常", "result": "pass"},
    {"id": 2, "case_name": "密码错误", "result": "fail"}
]

with open("result.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()  # 写入表头
    writer.writerows(rows)
'''
六、高频考点 & 坑点总结

1.
newline = ""：写csv不加，Windows每行之间出现空白行。
2.
编码
-  utf‑8 ：记事本打开中文乱码
-  utf‑8‑sig ：兼容Excel直接打开不乱码（测试优先用这个）
3.
csv只能处理文本，不能直接存图片、二进制。
4.
reader / DictReader
只能遍历一次，遍历完指针到文件末尾，再次读取需要重新打开文件或者转存为列表。'''

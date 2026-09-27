'''5. os 模块
 1知识说明
os 模块常用于操作文件、目录和系统环境。
2 常用函数
• os.getcwd()：获取当前路径
• os.listdir()：列出目录内容
• os.mkdir()：创建目录
• os.makedirs('a/b/c/d/f')：创建多层级目录
• os.remove()：删除文件
• os.path.isfile()：判断是否是文件
• os.path.isdir(): 判断是否是文件夹
• os.path.join(): 拼接路径
• os.path.exists("test.txt") : 判断文件或者文件夹是否存在
• os.path.basename(path)'''
import os
print(dir(os))
# 打印当前工作路径
print(os.getcwd())
# 拼接路径：当前目录下，logs‑>run.log它只负责拼字符串，不会检查文件是否真的存在
print(os.path.join(os.getcwd(),'logs','run.log'))
print(os.path.join('logs','run.log'))
# 3. 判断 run.log 是否存在
print(os.path.exists('logs/run.log'))
# 4. 判断 run.log 是否是文件
# 4. 新建文件夹 order_data
# os.mkdir("order_data")

# 5. 一次性创建目录 order_data/2026/06（嵌套多层）
# os.makedirs("order_data/2026/06")

# 6. 列出当前文件夹内所有内容
print(os.listdir())

# 7. 判断 order_data 是否为文件夹
print(os.path.isdir("order_data"))   # True

# 8. 取出路径 D:/project/test.py 的文件名
print(os.path.basename("D:/project/test.py"))   # test.py

# 9. 删除空文件夹 order_data
# os.rmdir("order_data")

# 10. 写分支：不存在则新建logs文件夹，存在就跳过
# if not os.path.exists("logs"):
#     os.mkdir("logs")
#     print("logs 已创建")
# else:
#     print("logs 已存在，跳过")
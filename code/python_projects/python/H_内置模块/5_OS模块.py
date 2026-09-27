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
'''1. 文件操作基础
1 知识说明
文件操作常用于：
• 读取测试数据
• 保存执行日志
• 写入测试结果
• 生成报表
• 处理配置文件
2 基本步骤
1. 打开文件
2. 读取或写入
3. 关闭文件
 3 open() 语法
open(file, mode, encoding)读取整个文件
f = open("test.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()  # 必须关闭释放资源

读取一行
f = open("test.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print(line1, line2)
f.close()

读取所有行，返回列表
f = open("test.txt", "r", encoding="utf-8")
lines = f.readlines()
print(lines)
f.close()
open() 与 with open() 的区别
open()
需要手动关闭文件
with open()
推荐方式，自动关闭文件
42.4 常见模式
模式作用特点
r只读（默认）文件不存在报错
w只写清空原有内容，无文件自动创建
a追加写入在末尾新增，不清空
r+读写文件必须存在，可读可覆盖
w+读写先清空再读写
a+追加读写末尾写入，支持读取
b二进制（rb/wb/ab）图片、视频、压缩包，不用写encoding
f.seek(0) 光标移动到开头
f.tell(  ) 查询光标当前位置'''
'''4. 文件指针移动 seek() / tell()
文件指针移动 seek() / tell()
• f.tell() ：获取当前指针位置
• f.seek(offset, whence) ：移动指针
• whence=0：从头偏移（默认）
• whence=1：从当前位置（仅二进制可用）
• whence=2：从文件末尾（仅二进制可用）
• utf-8 中文占 3 字节，seek 按字节移动，不要按字符数计算；'''
# with open("demo.txt", "r+", encoding="utf-8") as f:
#     print(f.tell())  # 初始0
#     f.write("abc123")
#     print(f.tell())  # 指针在末尾6
#     f.seek(0)        # 指针移到开头
#     print(f.read())
'''例：读取文件最后5个字符'''
# with open("demo.txt", "rb") as f:
#     f.seek(-5, 2)
#     print(f.read().decode("utf-8"))seek 的 -5 是"字节数"，不是"字符数"。只有文件全是英文/数字（1字符=1字节）时 -5 才刚好是 5 个字；中文 1 字=3 字节，-5 必然切字。
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 文本模式：按字符读
    print(content[-5:])       # 切片也是按字符：安全拿到最后5个字

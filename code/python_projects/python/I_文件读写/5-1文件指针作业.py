# 1. 写文件 → 读前6字符 → 打印指针 → 重置再读全部
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("MonkeyTest_ANR_Crash")

with open("log.txt", "r", encoding="utf-8") as f:
    print("前6个字符:", f.read(6))        # MonkeyT
    print("当前指针位置:", f.tell())      # 6（英文1字符=1字节）
    f.seek(0)                            # 重置到开头
    print("全部内容:", f.read())          # MonkeyTest_ANR_Crash

# 2. rb 模式 seek 到倒数4字节
with open("content.txt", "wb") as f:
    f.write(b"1234567890")

with open("content.txt", "rb") as f:
    f.seek(-4, 2)                        # 末尾往前4字节
    print(f.read())                      # b'7890'

# 3. 验证：a 模式打开指针不在 0
with open("log.txt", "a", encoding="utf-8") as f:
    print("a模式打开后指针位置:", f.tell())  # 19（log.txt末尾）→ 证明a模式指针在末尾

# 4. 读3字符 → 指针往后移2字节 → 读剩余
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("abcdefgh")

with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read(3))                     # abc（指针到3）
    f.seek(2, 1)                         # 从当前位置3往后2 → 5
    print(f.read())                      # fgh（下标5开始）

# 5. 函数：seek+tell 获取文件总字节大小
def get_file_length(file_path):
    with open(file_path, "rb") as f:
        f.seek(0, 2)                     # 跳到末尾
        return f.tell()                  # 末尾位置 = 文件大小

print("content.txt 字节数:", get_file_length("content.txt"))   # 10

# 6. 逐行读完指针在末尾 → 重置指针再读
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
    print("读完后指针位置:", f.tell())    # 末尾
    f.seek(0)                            # 不用重开文件，重置即可
    print("再次读取:", f.read())

# 7. UTF-8 汉字3字节，跳转到第3个汉字开头
with open("word.txt", "w", encoding="utf-8") as f:
    f.write("测试数据")                   # 测(0-2) 试(3-5) 数(6-8) 据(9-11)

with open("word.txt", "rb") as f:
    f.seek(6)                            # 第3个汉字"数"从字节6开始（0起算）
    print(f.read().decode("utf-8"))      # 数据

# 8. 测试：文本模式能否 seek(0,2)
with open("data.txt", "r", encoding="utf-8") as f:
    try:
        f.seek(0, 2)                     # 文本模式【允许】seek(0,2)
        print("seek(0,2) 成功，指针在末尾:", f.tell())   # 8
    except Exception as e:
        print("文本模式不支持末尾基准:", e)

with open("data.txt", "r", encoding="utf-8") as f:
    try:
        f.seek(5)                        # 真正不支持的是【任意偏移】
    except Exception as e:
        print("捕获报错:", type(e).__name__, "-", e)   # io.UnsupportedOperation

# 9. 读第一行 → 记录字节长度 → 跳第二行第2个字符后读剩余
with open("monkey.log", "rb") as f:
    first = f.readline()
    print("第一行:", first.decode().strip())
    print("第一行字节长度:", len(first))   # 字节长度（含换行）
    f.read(2)                            # 指针已在第二行开头，跳过2个字节
    print("剩余内容:", f.read().decode())

# 10. 函数：二进制读取最后 n 字节
def read_last_n_byte(file_path, n):
    with open(file_path, "rb") as f:
        f.seek(-n, 2)                    # 末尾往前 n 字节
        return f.read()

print(read_last_n_byte("content.txt", 4))   # b'7890'

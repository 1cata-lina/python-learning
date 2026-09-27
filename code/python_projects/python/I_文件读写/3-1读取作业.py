'''细节	说明
read vs readline vs readlines	read() 全部→字符串；readline() 一次一行→字符串；readlines() 全部→列表。注意单词带不带 s
空行 ≠ 读取结束	空行是 "\n"（为真），只有读到文件末尾才返回 ""（为假）—— 第 2 题 if not line 不会在空行误停，这是经典考点
空行清洗	第 7 题 if line.strip()：空行 strip 后是 "" → 为假跳过；有内容的行 strip 后非空 → 保留
rb 模式	读图片 / 视频不能指定 encoding（二进制没有字符编码），返回的是 bytes 字节
为什么大文件用 for	f.read() 会把整个文件塞进内存，几百 MB 日志会爆内存；for line in f 一次只读一行，内存恒定
为什么第 10 题用 sum(1 for line in f)	比 len(f.readlines()) 省内存 —— 后者把所有行都装进列表了，日志大时会卡
with 的魔力	with open(...) as f: 缩进结束自动 close()，忘写 f.close() 也不会泄漏文件句柄'''
# 1. read() 全量读取
with open("api_log.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 一次读完，返回字符串
    print(content)

# 2. readline() 单行循环读取
with open("error.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()   # 每次读一行
        if not line:          # 读到末尾返回空字符串"" → 停止
            break
        print(line.strip())

# 3. readlines() 读取所有行成列表
with open("black_pkg.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()     # 返回 ['包名1\n', '包名2\n', ...]
    for pkg in lines:
        print(pkg.strip())    # strip 去掉换行再打印

# 4. for 循环逐行读取（大文件最优，不占内存）
with open("monkey_run.log", "r", encoding="utf-8") as f:
    for line in f:            # 迭代文件对象，一次只读一行进内存
        if "ANR" in line:     # 过滤包含 ANR 的日志
            print(line.strip())

# 5. with 上下文读取（自动关闭，不用 close）
with open("user_info.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# 缩进结束后文件自动关闭，无需手动 f.close()

# 6. strip() 清除换行，存入设备列表
devices = []
with open("device_list.txt", "r", encoding="utf-8") as f:
    for line in f:
        devices.append(line.strip())   # 去掉 \n 和空格
print(devices)

# 7. 过滤空行，只保留有效记录
with open("test_record.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():      # 空行 strip 后是 ""，为假 → 跳过
            print(line.strip())

# 8. rb 二进制模式读取图片
with open("screen.png", "rb") as f:   # rb 不用指定 encoding
    data = f.read()           # 字节数据 bytes
    print(len(data))          # 文件字节长度

# 9. 只读前 5 行
with open("request.log", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= 5:            # 读到第 6 行就停
            break
        print(line.strip())

# 10. 统计两个文件各自行数
with open("success.log", "r", encoding="utf-8") as f:
    success_count = sum(1 for line in f)   # 逐行计数，不占内存
with open("fail.log", "r", encoding="utf-8") as f:
    fail_count = sum(1 for line in f)
print(f"成功日志 {success_count} 行，失败日志 {fail_count} 行")

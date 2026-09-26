'''
time 模块用于处理时间戳、格式化时间、延时等。
1. time.sleep(n) 暂停程序 n 秒
2. time.time() 时间戳（浮点数，从1970-01-01至今秒数）
3. time.localtime() 本地时间元组
4. time.strftime() 格式化时间（最常用）
5. time.ctime() 简易可读时间字符串
6. time.strptime()  转换为时间结构的元组
'''
import time
# 路线 2：时间戳 → localtime () → 元组 → strftime () → 字符串
# 取时间戳获取【当前时间戳】浮点数（从1970-01-01 UTC到现在的秒）
ts = time.time()
# 2. 时间戳 → localtime() → struct_time元组
tup = time.localtime(ts)
print("时间元组：", tup)
# 3. struct_time元组 → strftime() → 时间字符串
s = time.strftime("%Y-%m-%d %H:%M:%S", tup)
print("时间字符串：", s)

# 路线 1：字符串 → strptime () → 元组 → mktime () → 时间戳
# struct_time元组→转时间字符串
timeStr1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# 字符串转struct_time strptime：字符串 → 元组
st = time.strptime(timeStr1, "%Y-%m-%d %H:%M:%S")


# 1.时间字符串
time_str = "2026-09-26 10:00:00"
# 2.strptime：字符串转struct_time元组
time_tuple = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("strptime结果：", time_tuple)
# 3.mktime：struct_time元组转时间戳
timestamp = time.mktime(time_tuple)
print("mktime时间戳：", timestamp)
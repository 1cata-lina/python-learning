'''# time模块6个函数完整讲解（按你列的顺序，精简好背）
```python
import time
```
## 1. time.sleep(n)
**作用：让程序暂停、休眠 n 秒，n可以是小数**
```python
print("开始")
time.sleep(2)   # 停2秒
print("结束")
```
- 特点：**阻塞等待**，程序卡在这，啥也不干，等到时间到才往下跑
- 自动化测试最常用：等待页面/设备响应
> 例：`time.sleep(0.5)` 休眠0.5秒

## 2. time.time()
**作用：获取当前时间戳，浮点数，代表从1970-01-01 UTC零点到现在的总秒数**
```python
ts = time.time()
print(ts) # 输出类似：1795689321.123456
```
- 用途：计算代码运行耗时、日志记录时间戳
```python
start = time.time()
time.sleep(1)
end = time.time()
print(end - start) # 算出执行花费多少秒
```

## 3. time.localtime([时间戳])
**作用：把时间戳 → 本地时区 struct_time 时间元组；不传参默认取当前时间**
```python
tup = time.localtime()
print(tup)
# time.struct_time(tm_year=2026, tm_mon=9, tm_mday=26, tm_hour=21, ...)
```
可以单独取年、月、日：`tup.tm_year`
> 对比：`time.gmtime()` 是UTC世界时间，比北京时间晚8小时

## 4. time.strftime(格式, [时间元组])
**作用：struct_time元组 → 格式化时间字符串（f=format格式化）**
```python
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(s) # 2026-09-26 21:35:20
```
常用格式符：
- `%Y`4位年，`%m`月，`%d`日
- `%H`24小时，`%M`分钟，`%S`秒

## 5. time.ctime([时间戳])
**作用：时间戳 → 简易可读时间字符串；不传参默认当前时间**
```python
print(time.ctime())
# 输出：Sat Sep 26 21:36:10 2026
```
- 不用自己写格式，直接得到英文样式时间字符串
- 底层等价：`asctime(localtime(时间戳))`
- 缺点：样式固定，**不能自定义年月日顺序**，需要自定义格式就用strftime

## 6. time.strptime(时间字符串, 格式)
**作用：时间字符串 → struct_time时间元组（p=parse解析）**
```python
t = time.strptime("2026-09-26 21:35:20", "%Y-%m-%d %H:%M:%S")
print(t)
```
⚠️重点坑：**格式字符串必须和时间字符串完全匹配**
字符串是`2026/09/26`，格式就必须写`%Y/%m/%d`，写`-`会直接报错。

---
# ✅ 极简背诵总结
1. `sleep(n)`：休眠，程序停n秒
2. `time()`：拿时间戳（浮点数秒）
3. `localtime()`：时间戳→本地时间元组
4. `strftime(格式,元组)`：元组→自定义时间字符串（格式化）
5. `ctime()`：时间戳→固定样式英文时间字符串
6. `strptime(字符串,格式)`：时间字符串→时间元组（解析）

## 流转关系串起来
`time.time()` →时间戳 →`localtime()`→元组 →`strftime()`→自定义字符串
字符串 →`strptime()`→元组 →`mktime()`→时间戳
`time.ctime()`：时间戳一键转现成字符串

'''
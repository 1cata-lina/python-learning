# 案例1：提取日志所有状态码
import re

log = """
request /login 200
request /list 500
request /detail 200
"""
codes = re.findall(r'\d{3}', log)
print(codes)
# 案例2：过滤接口报错，删除数字
text = "请求超时 408 服务器异常500"
clean = re.sub(r'\d+', '', text)
print(clean)
# 案例3：提取APP包名 com.xxx.xxx
msg = "启动com.wechat,崩溃com.tencent.mm"
pkgs = re.findall(r'com\.\w+\.\w+', msg)
print(pkgs)
'''八、匹配对象常用方法
匹配成功返回 Match 对象，可调用：
• .group() ：完整匹配内容
• .group(n) ：第n个分组内容
• .start() ：匹配起始下标
• .end() ：匹配结束下标
• .span() ：返回(起始,结束)元组'''
# 案例4日志/测试场景）
import re

# 1. 提取字符串中全部数字，返回列表
s1 = "today2026年6月16日"
print(re.findall(r"\d+", s1))          # ['2026', '6', '16']

# 2. 将所有中文替换为空
s2 = "today2026年6月16日"
print(re.sub(r"[\u4e00-\u9fa5]+", "", s2))   # today2026616（年月日被删掉）

# 3. 匹配11位手机号码，从日志中筛选
s3 = "today2026年6月16日，13312345678是有的手机号"
print(re.findall(r"1\d{10}", s3))      # ['13312345678']

# 4. 用 re.search 提取 http 状态码（status=xxx）
s4 = "status=200 code=503"
m = re.search(r"status=(\d+)", s4)
print(m.group(1))                      # 200（只取括号里的数字）

# 5. re.split 按空格、逗号、竖线分割
s5 = "user1,user2 user3|user4"
print(re.split(r"[ ,|]+", s5))         # ['user1', 'user2', 'user3', 'user4']

# 6. 预编译规则，循环读取多行日志提取报错码
log = """request /login 200
request /list 500
request /detail 200"""
pattern = re.compile(r"request\s+(\S+)\s+(\d+)")   # 预编译，只编译一次
for line in log.splitlines():
    m = pattern.search(line)
    url, code = m.group(1), m.group(2)
    flag = "⚠️ 报错" if code != "200" else ""
    print(f"{url} -> {code} {flag}")
# 输出：/login -> 200 / /list -> 500 ⚠️ 报错 / /detail -> 200

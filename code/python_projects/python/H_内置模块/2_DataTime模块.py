import datetime
print (dir(datetime))
'''
from datetime import datetime, date, time, timedelta
1.  datetime ：年月日时分秒（最常用）
2.  date ：只处理年月日
3.  time ：只处理时分秒
4.  timedelta ：时间差，做加减运算
1. 获取当前完整时间（datetime）'''
from datetime import datetime

# 当前时间对象
now = datetime.now()
print(now)
# 单独取值
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
# 2. 格式化输出 strftime
now = datetime.now()
# 年-月-日 时:分:秒
t = now.strftime("%Y-%m-%d %H:%M:%S")
print(t)
s = "2026-06-10 12:30:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt, type(dt))
# 4. 时间加减 timedelta（比time模块方便）
from datetime import datetime, timedelta

now = datetime.now()
# 3天后
after3 = now + timedelta(days=3)
# 2小时前
before2h = now - timedelta(hours=2)
# 10分钟后
t10 = now + timedelta(minutes=10)

print("3天后：", after3.strftime("%Y-%m-%d %H:%M:%S"))

'''5. date 只操作日期'''
from datetime import date
today = date.today()
print(today, today.year, today.month, today.day)
# 7天前
last7 = today - timedelta(days=7)
print(last7)
'''6. time 只操作时分秒'''
from datetime import time
t = time(14, 20, 30)
print(t.hour, t.minute, t.second)
'''7. 时间戳互转'''
from datetime import datetime
now = datetime.now()
# datetime → 时间戳
ts = now.timestamp()
print(ts)

# 时间戳 → datetime
dt = datetime.fromtimestamp(ts)
print(dt)

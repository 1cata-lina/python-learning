import random
import string
# 1. 生成 n 位大写字母验证码（chr(65~90) 对应 A~Z）
def a(n):
    return ''.join(random.choice(string.ascii_uppercase)for i in range (n))
print("大写字母n位验证码：",a(5))
# 2. 生成 n 位小写字母验证码
def b(n):
    return ''.join(random.choice(string.ascii_lowercase)for i in range (n))
print("小写字母n位验证码：",b(5))
# 3. 生成 n 位"字母+数字"混合验证码（用 string 库的字符集）
def c(n):
    return ''.join(random.choice(string.ascii_letters+string.digits)for i in range (n))
print("字母+数字n位验证码：",c(5))
# 4. 生成 n 位"不重复"数字验证码（sample 抽取，不能有重复）
def d(n):
    return ''.join(str(x) for x in random.sample(range(10), n))
print("不重复数字n位验证码：",d(5))
# 5. 掷骰子 n 次，返回点数列表（randint 造列表）`
# [每掷一次的结果 for 掷多少次]` → 返回 "结果列表"。
def e(n):
    return [random.randint(1,6) for i in range(n)]
print("掷骰子n次结果列表：",e(5))
## 6. 生成 n 个 1~100 随机整数列表
def f(n):
    return [random.randint(1,100)for i in range(n)]
# 7. 从列表里随机抽 n 个元素（允许重复）
def pick(li, n):
    return [random.choice(li) for i in range(n)]
# 8. 双色球式：从 1~33 抽 6 个不重复数字并排序
def lottery():
    return sorted(random.sample(range(1, 34), 6))
# 9. 生成 n 个 0~1 随机小数列表
def rand_floats(n):
    return [random.random() for i in range(n)]
# 10. 随机密码：8 位，数字+大小写字母
def password(n=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))



# 生成 0~1 的随机浮点数并打印
import random
a=random.random()
print("1.随机浮点数：",a)
# 输出 1~100 之间随机整数
b=random.randint(1,100)
print("2.随机整数1-100：",b)
# 生成 10~30 之间随机偶数
c=random.randrange(10,30,2)
print("3.随机偶数10-30：",c)
# 随机生成 5.0 ~ 10.0 的小数
d=random.uniform(5.0,10.0)
print("4.随机小数5.0~10.0：",d)
# 列表 ["篮球","足球","羽毛球"] 随机抽一个运动
e=random.choice(["篮球","足球","羽毛球"])
print("5.随机运动：",e)
# 列表 [10,20,30,40,50] 随机取出 3 个不重复数字
f=random.sample([10,20,30,40,50],3)
print("6.随机不重复数字3个：",f)
# 定义数字列表 1~100，使用 shuffle 打乱顺序后打印
g=[i for i in range(1,101)]
c=random.shuffle(g)
print("7.打乱顺序后的数字列表：",g)
# 设置种子seed=10，循环10次生成(1,20)之间的随机整数，观察结果
seed=10
random.seed(seed)
for i in range(10):
    print("8.随机整数(1,20)：",random.randint(1,20),end=" ")
print()
# 循环 5 次，每次输出一个 0~9 随机数字
for i in range(5):
    print("9.随机数字0~9：",random.randint(0,9),end=" ")
# 编写函数，传入长度 n， 返回 n 位数字随机验证码字符串

def rand_code(n):
    return ''.join(random.choice('0123456789') for i in range(n))
print("10.随机验证码：",rand_code(6))
def get_code(n):
    code = ""
    for i in range(n):
        code += str(random.randint(0, 9))
    return code
print(get_code(6))   # 例如输出 6 位验证码
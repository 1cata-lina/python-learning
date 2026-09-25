'''
当需要遍历一个序列，或者循环次数明确时，通常使用 for。
for 变量 in 可迭代对象:
    循环体

'''
# 遍历字符串
s = "Python"
for ch in s:
    print(ch)

 # 遍历列表
names = ["张三", "李四", "王五"]
for name in names:
    print(name,end="\t")
print()
# 遍历字典
user = {"name": "张三", "age": 18}
for k in user:
    print(k,end="\t")#不管填什么都是默认拿字典的键key的
print()
for value in user.values():
    print(value,end="\t")
print()
for key, value in user.items():
    print(key, value,end="\t")
# range() 函数 range(开始, 结束, 步长)
for i in range(5):print(i)
for i in range(1, 6): print(i)
for i in range(0, 10, 2):print(i)
for i in range(5, 0, -1): print(i)#5\4\3\2\1
for i in range(10, 2, -2):print(i)#10\8\6\4\下一个是 2，等于 stop，停止，不打印 2

# 循环嵌套循环内部再套循环，适合处理二维结构、表格、矩阵、乘法表等。
for i in range(5):
    for j in range(7):
        print("*", end=" ")
    print()
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end="\t")
    print()
users = ["test01", "test02", "test03"]
passwords = ["123456", "admin123"]
for user in users:
    for pwd in passwords:
        print(f"用户名：{user}，密码：{pwd}")

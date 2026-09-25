'''
推导式可以快速生成新的列表、集合、字典，让代码更简洁。
无条件
[表达式 for 变量 in 可迭代对象]
带if条件筛选
[表达式 for 变量 in 可迭代对象 if 条件]
多分支if-else（写在前面）
[满足if的结果 if 条件 else else结果 for 变量 in 可迭代对象]
双层循环
[表达式 for 变量1 in 序列1 for 变量2 in 序列2]
'''

# [表达式 for 变量 in 可迭代对象]
# [表达式 for 变量 in 可迭代对象 if 条件]
nums = [i for i in range(1, 6)]
print(nums)
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)
double_evens = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(double_evens)
#
names = ["tom", "jerry", "wendy", "bob"]
result = [name.upper() for name in names if len(name) > 3]
print(result)
# 集合推导式
names = ["tom", "jerry", "tom", "bob"]
result = {name.upper() for name in names}
print(result)
#
modules = ["登录", "注册", "支付", "登录"]
result = {module for module in modules}
print(result)
# 字典推导式{key:value for 变量 in 可迭代对象}：**遍历里面每一个元素，每循环一次，生成一对 key:value，最后全部打包成字典**
nums = [1, 2, 3, 4]
result = {i: i * i for i in nums}
print(result)
users = ["test01", "test02", "test03"]
user_dict = {user: "123456" for user in users}
print(user_dict)
result = {i: i * i for i in nums}
'''`result[i] = i * i`：**往字典 result 里面，新增 / 修改一对键值对。**
`result[键] = 值`，这是字典最基础的赋值写法。'''

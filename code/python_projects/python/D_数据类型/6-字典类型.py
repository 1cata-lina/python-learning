'''
字典用于存储键值对数据，格式如下：{键: 值}
• 键必须唯一
• 值可以重复
• 通过键来访问值
• 非常适合表示结构化数据
'''
user = {
    "username": "admin",
    "password": "123456",
    "age": 18
}
user = {
    "username": "admin",
    "password": "123456"
}

print(user["username"])
# print(user["u"])
print(user.get("password"))
print(user.get("pa"))
print(user.get("email"))  # 不存在返回 None
# 添加与修改
user = {"username": "admin"}
user["password"] = "123456"
user["username"] = "test01"
print(user)

# 删除数据
user = {"username": "admin", "password": "123456", "age": 18}
del (user["age"])
print(user)

"""常用方法
• keys()
• values()
• items()
• get()"""

# 示例字典
student = {"name":"小明", "age":22, "city":"重庆"}

## 1. keys () → 获取字典所有【键】
# 拿到字典里面所有 key，返回一个可迭代对象
print(student.keys())
# dict_keys(['name', 'age', 'city'])
# 遍历
for k in student.keys():
    print(k)
## 2. values () → 获取字典所有【值】拿到字典里面所有 value
print(student.values())
# dict_values(['小明', 22, '重庆'])
for v in student.values():
    print(v)
## 3. items () → 获取【键值对】，返回 (key,value) 元组循环遍历字典必用
print(student.items())
# dict_items([('name', '小明'), ('age', 22), ('city', '重庆')])

# 拆包遍历
for k, v in student.items():
    print(f"键{k}, 值{v}")
    # 不拆包，先接收整个元组
for item in student.items():
        k = item[0]
        v = item[1]
        print(f"键{k}, 值{v}")
## 4. get () → 根据 key 取值，重点！和 `dict[key]` 的区别
# 语法：`字典.get(key, 默认值)`
'''
- 如果 key 存在：返回对应 value
- 如果 key**不存在：不会报错！** 返回 None，或者你指定的默认值
> 对比：`student["height"]` 找不到 key 直接报错！'''

print(student.get("name")) # 小明，key存在
print(student.get("height")) # None，找不到不报错
print(student.get("height", 170)) # 找不到，返回默认值170

device_info = {
    "dev01":{"id":"ECU01", "battery":15},
    "dev02":{"id":"ECU02", "battery":80}
}
for dev_k,dev_v in device_info.items():
    print(f"设备代号：{dev_k}")
    for sub_k,sub_v in dev_v.items():
        print(f"  {sub_k}: {sub_v}")
'''
# 第一层循环：遍历外层字典 device_info.items()
for dev_key, dev_data in device_info.items():
    # dev_key：外层的key，也就是 "dev01"、"dev02"
    # dev_data：外层的value，也就是内层的子字典
    
    print(f"设备代号：{dev_key}")
    # 第二层循环：遍历内层子字典 dev_data.items()
    for sub_k, sub_v in dev_data.items():
        print(f"  {sub_k}: {sub_v}")


'''
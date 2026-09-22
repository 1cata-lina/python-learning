'''
字符串是用括号括起来的一段文本内容
切片
字符串【开始：结束：步长】
`join`是**分隔符**，
插在元素**中间**，元素数量≥2，才能看到分隔符
'''
name="zhangshan"
sesc="自动化测试"
print(name+sesc)
print(name[0])
print(name[1])
print(sesc[1])
print(sesc[-1])
# 切片
s="chong qing"
print(s[-4:])
print(s[0:4:1])
print(s[::-1])
print(s[::1])
print(s[0:])
print(dir(s))
#字符串常用方法
s="flower Sumsunsum"
print(s.upper())#转大写
print(s.lower())#转小写
print(s.title())#首字母大写
print(s.isalpha())#是否全字母
print(s.isdecimal())#是否全数字
print(s.isdigit())#是否全数字
print(s.count("s"))#统计次数
print(s.find("f"))#查找，找不到返回-1
print(s.index("s"))#查找，找不到报错
print(s.count("s"))#统计次数
print(s.rfind("s"))#从右边开始查找

print(s.replace("s","z"))#替换
print(s.split())#分隔
print(s.strip())#去掉空格
print("liq".join("123"))#1liq2liq3
print("".join(["flower","Sumsunsum"]))#flowerSumsunsum
print(s.startswith("flower"))#是否以什么开头
print(s.endswith("flower"))#是否以什么结尾

username="userone"
if username.isalpha()==True and len(username)<=10:
    print("用户名格式正确")
else:
    print("用户格式错误")
print(f"{username.count("e")}查询字符串出现的次数")
# 将 "2025-06-01" 按 - 分割
date_1="2025-06-01"
print(date_1.split("-"))
print(date_1.isdecimal())
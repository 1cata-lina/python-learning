'''
身份运算符用于判断两个对象是否是同一个对象。
• is
• is not
'''
a=[1,2]
b=[2,3]
c=a
print(a==b)
print(a is b)
print(a is not b)

#案例：判断变量是否为空对象
result=None
if result is None:
    print("接口返回对象为空")
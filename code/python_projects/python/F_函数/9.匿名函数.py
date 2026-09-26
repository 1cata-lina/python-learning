# 匿名函数lambda 参数列表 : 表达式
def add(x,y):
    return x + y
# 等价
lambda x,y : x + y
# 用法
new_func = lambda x,y : x + y
print(new_func(3,4))
#无参数
lambda : 100
#单个参数
lambda x:x*2
#多个参数
lambda x,y:x+y
#带默认值
lambda x,y=10:x+y
#可变位置参数 *args
lambda *args: sum(args)
#可变关键字参数 **kwargs
lambda **kwargs: kwargs.get("name")


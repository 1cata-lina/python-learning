# return 返回值如果函数内部计算的结果要在外部继续使用，需要 return
# 返回。`return`：**把函数里面的数据，送回到函数调用的地方；
# 同时，执行到 return，函数直接结束，后面代码不会跑。**
# > `print`：只是把内容打印在屏幕，数据用完就没了，外面拿不到。
# > `return`：把结果**返回出来**，你可以用变量接住，继续做计算、判断。
'''
1.一旦执行 return，函数立刻终止！return 后面的代码不会执行
2.return 可以一次性返回多个值，多个返回值会自动打包成元组
3.如果没有`return`，函数默认返回`None`，外面接不到计算结果
'''

def add(a, b):
    return a + b
result = add(10, 20)
print(result)
# 返回多个值
def get_user():
    return "admin", "123456"
result = get_user()
print(result)
#有返回值可以对函数进行之后的计算
# 题目1定义函数get_pi，无参数，返回圆周率3.14，调用函数接收并打印数值。
def get_pi():
    return 3.14
result = get_pi()
print(result)
# 题目2定义函数add，接收两个数字a、b，返回两数之和，外部打印相加结果。
def add(a, b):
    return a+b
result = add(10, 20)
print(result)
# 题目3定义函数get_msg，接收name，返回拼接字符串f"你好{name}"，外部打印返回的问候语。
def get_msg(name):
    return f"hello\t{name}"
result = get_msg("cqld")
print(result)
# 题目4定义函数max_two，接收x、y，返回两个数中较大的数字。
def max_two(x,y):
    return max(x,y)
result = max_two(10,20)
print(result)
# 题目5定义函数rect_area，接收长length、宽width，返回长方形面积。
def rect_area(length,width):
    return length*width
result = rect_area(10,20)
print(result)
# 题目6定义函数get_info，接收姓名name、年龄age，同时返回两个数据，外部拆包打印。
def get_info1(name,age):
    return name,age
list1={'name':'zhangsan','age':18}
result=get_info1(**list1)
print(result)
name_val, age_val = get_info1(**list1)
print(name_val) # zhangsan
print(age_val)  # 18
# 题目7定义函数judge_num，接收数字n，如果大于0返回"正数"，小于0返回"负数"，等于0返回"零"。
def judge_num(n):
    if n>0:
        return "正数"
    elif n<0:
        return "负数"
    else:
        return "零"
result=judge_num(19)
print(result)
# 题目8定义函数calc_avg，使用 * args接收任意多个数字，返回数字平均值。
def calc_avg(*args):
    return sum(args)/len(args)
result=calc_avg(1,2,3,4)
print(result)
# 题目9定义函数default_greet，参数name，msg默认值为"早上好"，返回拼接好的问候语句。
def default_greet(name,msg="早上好"):
    return (f"{name} {msg}")
result= default_greet("cqld")
print(result)
# 题目10定义函数get_dict， ** kwargs接收任意学生信息，把收到的字典直接返回，外部打印字典。
def get_dict(**kwargs):
    return kwargs
list2={'name':'zhangsan','age':18}
result=get_dict(**list2)
print(result)
# 不定长参数接收多个位置参数，结果是元组。*args
def show_args(*args):
    print(args)
show_args(1, 2, 3, "hello")
# **kwargs 接收多个关键字参数，结果是字典。
def show_kwargs(**kwargs):
    print(kwargs)
show_kwargs(name="张三", age=18)
# 比如写一个求和函数，不知道用户会传几个数字进来
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
# 再比如打印人员信息，每个人信息字段不一样：有的人有年龄，有的人有地址
def print_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
print_info(name="小明",age=20)
print_info(name="小红",city="重庆",phone="123456")
# `*` 和 `**` 在调用函数的时候还有**解包**作用，这个后面学。
## 1. `*` 解包：把列表 / 元组 / 可迭代对象拆开成【位置参数】
# `*` 作用：把一个容器里面的元素**拆出来，单独当成一个个位置参数传入**(重要)
# 区分两个场景：
# 1. **定义函数时**：`def func(*args, **kwargs)` → **打包**，把多个参数打包成元组 / 字典
# 2. **调用函数时**：`func(*my_list, **my_dict)` → **解包**，把容器拆开，一个个传给函数

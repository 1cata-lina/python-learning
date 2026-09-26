# Python `*args` / `**kwargs` 笔记整理（精简版，适合面试+车载测试Python复习）
#核心区分：**def定义函数时 = 打包；调用函数括号内 = 解包**
## 一、不定长参数（打包）不知道函数未来接收多少参数时使用
### 1. `*args`接收**多个位置参数**，打包成**元组 tuple**

def show_args(*args):
    print(args)
show_args(1, 2, 3, "hello")
# 输出：(1, 2, 3, 'hello')
# 位置参数：只写值，`函数(值1,值2)`，不带`key=值`✅示例：求和函数，参数数量不固定
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))


### 2. `**kwargs`接收**多个关键字参数（key=value）**，打包成**字典 dict**

def show_kwargs(**kwargs):
    print(kwargs)
show_kwargs(name="张三", age=18)
# 输出：{'name': '张三', 'age': 18}关键字参数：`函数(键1=值1,键2=值2)`
def print_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

print_info(name="小明",age=20)
print_info(name="小红",city="重庆",phone="123456")


### 3. 组合写法 `*args, **kwargs`同时接收任意数量位置参数 + 关键字参数
# 参数顺序强制：普通参数 → *args → **kwargs**，不能颠倒
def all_param(*args,**kwargs):
    print("args元组：", args)
    print("kwargs字典：", kwargs)

all_param(1,2,3,name="李四",gender="男")
# args元组： (1, 2, 3)
# kwargs字典： {'name': '李四', 'gender': '男'}

# 补充：`args`、`kwargs`只是约定俗成名字，可以自定义变量名，但是行业统一习惯写args/kwargs。

## 二、调用函数时：`*` 和 `**` 【解包】
"""解包：把容器（列表/元组/字典）拆开，把里面元素单独拿出来，作为参数传入函数
注意：**解包是发生在调用阶段，不是函数定义！
"""
### 1. `*` 解包列表/元组（可迭代对象）把列表/元组拆开，变成一个个独立**位置参数**

def add(a,b,c):
    print(a+b+c)
nums = [10,20,30]
add(*nums)   # 等价 add(10,20,30)

# `*nums`：拆开列表外壳，取出里面元素，列表本身消失
# 元组同样可以用`*`解包：

nums_tuple = (1,2,3)
add(*nums_tuple)


# 搭配`*args`示例：

def show_args(*args):
    print(args)
my_list = [1,2,3]
show_args(*my_list)
# 等价 show_args(1,2,3)
# 输出：(1, 2, 3)
'''> ❗对比（不解包）'''

def test(*args):
    print(args)
lst = [1,2,3]
test(lst)
# 没有*，直接把整个列表当成1个参数传入
# 输出：([1, 2, 3],)  元组里面嵌套列表


### 2. `**` 解包字典
'''把字典的`key:value`拆开，变成`key=value`**关键字参数**传入函数
> ⚠️`**`只能解包字典，不能用于列表元组！
'''
def print_info(name, age):
    print(name, age)

info = {"name":"张三", "age":18}
print_info(**info)   # 等价 print_info(name="张三", age=18)

# 搭配`**kwargs`示例：

def show_kwargs(**kwargs):
    print(kwargs)
my_dict = {"city":"重庆","job":"测试"}
show_kwargs(**my_dict)
# 等价 show_kwargs(city="重庆", job="测试")
# 输出：{'city': '重庆', 'job': '测试'}


## 三、打包 + 解包 混合完整示例

# ========== 定义函数：* / ** 【打包】 ==========
def func(*args, **kwargs):
    # 收到多个位置参数 → 打包进args元组
    # 收到多个关键字参数 → 打包进kwargs字典
    print(args, kwargs)

# ========== 调用函数：* / ** 【解包】 ==========
list_data = [1,2]
dict_data = {"name":"李四"}
func(*list_data, **dict_data)
# 等价 func(1, 2, name="李四")
# 输出：(1, 2) {'name': '李四'}

'''> 流程拆解：
> 1. `*list_data`：解包列表，拆成位置参数`1,2`
> 2. `**dict_data`：解包字典，拆成关键字参数`name="李四"`（字典外壳被拆掉）
> 3. 进入函数，`*args`把`1,2`打包成元组；`**kwargs`把`name="李四"`打包成新字典'''

## 四、重要规则
'''1. `*`：可解包 list / tuple /字符串/集合；`*字典`只会取出字典的key
2. `**`：**只能解包字典**，其他类型报错
3. 函数调用时顺序：`*解包`写前面，`**解包`放后面，不能颠倒
4. 函数定义参数顺序：普通参数 → `*args` → `**kwargs`'''

## ✅一句话背诵
'''> 在`def`定义函数时，`*args`收集位置参数打包成元组，`**kwargs`收集关键字参数打包成字典；
> 在调用函数括号里面，`*`把可迭代对象解包成位置参数，`**`把字典解包成key=value关键字参数。'''



# 默认参数如果某个参数经常使用同一个值，可以设置默认值。
'''
## 1. 什么是默认参数
定义函数的时候，可以**给参数写一个默认值**。
👉 调用函数时：
- 如果传了这个参数的值 → 使用你传入的值
- 如果不传 → 自动使用定义时写好的**默认值**
## 多个参数，带默认的要放后面！【重点语法规则】
## 4. 超级大坑：不要用可变对象当默认参数！（面试高频坑）
可变对象：列表`[]`、字典`{}`、集合`set()`
> ⚠️ **没有默认值的普通参数，必须写在默认参数前面！**
def 函数名(参数名 = 默认值):
    函数体
'''
def register(username, role="tester"):
    print(f"用户名：{username}，角色：{role}")
register("zhangsan")
register("lisi", "admin")
# 题目1greet ，参数name，参数msg默认值为
# 早上好 ，打印：xx，xx
def greet(name,msg="早上好"):
    print(f"{msg} {name}")
greet("lisi")
# 题目2定义函数
#user_info ，参数name，sex默认
# 男 ，打印姓名和性别
def user_info(name,sex="男"):
    print(f"你好{name}性别{sex}")
user_info(name="lisi")
# 题目3定义函数
# print_line ，字符c默认 - ，长度num默认20，打印一串分割符号
def print_line(c="-",num=20):
    print(c*num)
print_line()
# 题目4 定义函数
# buy_goods ，参数goods，num默认1，打印：购买xx，数量xx件
def buy_goods(goods,num=1):
    print(f"购买{goods}数量{num}件")
buy_goods("牙膏")
# 题目5定义函数
# calc_area ，宽width，高height默认5，打印长方形面积
def calc_area(width,height=5):
    # print(width*height)
    return width*height
calc_area(5)
## return 的好处（为什么优先用 return）return 出来的结果**是数据，可以继续参与计算**：
'''
如果只用`print`，打印出来的只是屏幕上的文字，拿不到这个数字继续运算。
1. `print`：**展示给人看**，只输出到控制台，
无法继续拿这个数值计算
2. `return`：**返回给程序用**，
把计算结果交给调用方，不会自动显示；想要看到，需要额外 print 接收的返回值
'''
area = calc_area(5)
total = area + 10
print(total)
# 题目6定义函数
# room ，房间名room_name，人数people默认2，打印xx房间容纳xx人
def room(room_name,people=2):
    print(f"{room_name}房间容纳{people}人")
room("WW酒店")
# 题目7定义函数
# drink ，饮料名drink_name，甜度sweet默认正常 ，打印饮品和甜度
def drink(drink_name,sweet="正常"):
    print(f"饮品{drink_name}甜度{sweet}")
drink("可乐")
# 题目8定义函数car ，品牌brand，颜色color默认白色，打印车辆信息
def car(brand,color="color"):
    print(f"车辆是{brand}，颜色是{color}")
car("宝马","白色")
# 题目9定义函数lesson ，课程name，课时time默认45，打印课程与课时
def lesson(name,time="45"):
    print(f"{name}{time}")
lesson("数学")
# 题目10定义函数 tip ，内容text，符号symbol默认  # ，两边打印符号包裹文字
def tip(text,symbol="#"):
    print(f"{symbol}{text}{symbol}")
tip(1)


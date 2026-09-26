# 有参数函数参数让函数更灵活，可以接收外部传入的数据。
'''def 函数名(参数1, 参数2):
    函数体'''
def add(a, b):
    print(a + b)
add(10, 20)
# 题目1定义函数
# print_name ，接收1个参数name，打印：我的名字是xx
def print_name(name):
    print(f"我的名字是{name}")
print_name("lisi")
# 题目2定义函数 print_age ，接收参数age，打印：我今年xx岁
def print_age(age):
    print(f"我今年{age}岁")
print_age(18)
# 题目3定义函数student_info ，接收name、age两个参数，分行打印姓名和年龄
def student_info(name,age):
    print(f"我的名字是{name}",end="\t")
    print(f"我今年{age}岁")
student_info("lisi",18)
# 题目4 定义函数
# calc_add ，接收a、b两个数字，打印两数相加结果
def calc_add(a,b):
    return a+b
calc_add(199,20)
# 题目5 定义函数
# say_hello ，接收参数nickname，打印：你好，xx，欢迎光临
def say_hello(nickname):
    print(f"Hello {nickname}欢迎光临")
# 题目6定义函数
# food_tip ，接收food参数，打印：今天想吃xx
def food_tip(food):
    print(f"今天想吃xx{food}")
food_tip("寿司")
# 题目7定义函数
# rect ，接收长length、宽width，打印长方形周长
def rect(length,width):
    return length*width
rect(10,20)
# 题目8定义函数
# class_msg ，接收className、num两个参数，打印xx班一共有xx名学生
def class_msg(className,num):
    print(f"{className}班一共有{num}名学生")
class_msg(12,29)
# 题目9定义函数
# temp_show ，接收温度temp，打印当前室外温度：xx℃
def temp_show(temp):
    print(f"打印当前室外温度：{temp}℃")
temp_show(16)
# 题目10定义函数
# book_info ，接收书名book、价格price，打印书籍名称和售价
def book_info(book,price):
    print(f"书籍名称{book}售价{price}")
book_info("can网络",20)
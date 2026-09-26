# 无参数函数
def hello():
    print("欢迎学习 Python")
    print("今天学习函数")
hello()

# 题目1定义无参函数
# print_star，调用后打印一行10个星号： ** ** ** ** **
def print_star():
    for i in range(5):
        print("**",end="\t")
print_star()
print()
# 题目2定义无参函数 show_title，调用后输出： == == =学生管理系统 == == =
def show_title():
    print("== == =学生管理系统 == == =")
show_title()
# 题目3定义无参函数 print_info，依次打印三行文字：
# 姓名：张三
# 年龄：18
# 班级：一班
def print_info():
    print("姓名：张三")
    print("年龄：18")
    print("班级：一班")
print_info()
# 题目4定义无参函数say_morning，输出早安问候：早上好！新的一天加油
def say_morning():
    print("早上好！新的一天加油")
say_morning()
# 题目5定义无参函数 print_line，打印分割线：------------------------
def print_line():
    print("------------------------")
# 题目6定义无参函数 show_menu，打印简易菜单：
def show_menu():
    print("查询信息")
    print("修改信息")
    print("删除信息")
    print("退出程序")
show_menu()
# 题目7 定义无参函数 print_tri，打印简易三角形：
def print_tri():
    for i in range(1,3):
        print("*"* i)
print_tri()
# *
# **
#
# 题目8定义无参函数weather_tip，输出提示：今日下雨，出门记得带伞
def weather_tip():
    print("今日下雨，出门记得带伞")
weather_tip()
# 题目9 定义无参函数
# print_company，打印公司两行标语：
# 诚信经营
# 服务至上
def print_company():
    print("诚信经营")
    print("服务至上")
print_company()
# 题目10定义无参函数end_tip，打印结束提示：程序执行完毕，欢迎下次使用
def end_tip():
    print("程序执行完毕，欢迎下次使用")
end_tip()
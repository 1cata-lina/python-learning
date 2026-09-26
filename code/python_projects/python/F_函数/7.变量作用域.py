# 变量作用域变量作用域在函数外定义，通常整个模块都可使用。
name = "Python"
def show():
    print(name)
show()
# 局部变量 在函数内部定义，只能在函数内部使用
def test():
    age = 18
    print(age)
test()
'''1. **函数里面只读全局变量 → 不用写 global**
2. **函数里面要修改全局变量（赋值、+=、-=） → 必须写 global，放在函数最开头**
3. global 后面写变量名，**不能写等号赋值**'''
# global需要在函数内部修改全局变量时使用。Python：函数里面这个 `count`
# 告诉 ，不是函数内部新建的局部变量，而是外面那个全局变量。
count = 0
def add_count():
    global count
    count += 1
add_count()
print(count)
# 题目1定义全局变量
# name = "小明"，函数内部直接打印这个全局变量，调用函数。
name="小明"
def func_1(name):
    print(name)
func_1(name)
# 题目2全局变量money = 100，函数内部创建同名局部变量money = 50，分别在函数内外打印，观察区别。
money=100
def func_2():
    money = 50
    print("函数内:", money)
print("函数外(调用前):", money)   # 100
func_2()
print("函数外(调用后):", money)
# 题目3全局变量score = 0，使用global 在函数内让score加10，调用函数后打印全局score。
score=0
def func_3(n):
    global score
    score += n
func_3(10)
print(score)
#----------------------------------------------------------------------------
score=0
def func_4(s,n):
    return s+n
score=func_4(score,10)
print(score)
# 题目4函数内部定义局部变量msg = "hello"，尝试在函数外面打印msg，说出运行结果。
def func_5():
    msg="hello"
func_5()
# print(msg)
# 题目5全局变量height = 170，函数内不使用global，直接赋值height = 180，打印内外height对比。
height=170
def func_6():
    height=180
print(height)
func_6()
print(height)
# 题目6定义全局变量total = 0，写函数add_num(n)，global修改total，每次传入数字累加，调用3次后打印total。
total=0
def add_num(n):
    global total
    total += n
add_num(10)
add_num(20)
add_num(30)
print(total)
# 题目7word = "蓝天"，函数内用global把word修改为"白云"，调用后输出word。
word="蓝天"
def fuc_7():
    global word
    word="白云"
    print(word)
fuc_7()
print(word)
# 题目8函数内定义局部列表lst = [1, 2, 3]，函数内打印，外部访问lst看是否报错。
lst=[1,2,3]
def func_8():
    print(lst)
func_8()
print(lst)
# 题目9全局age = 18，函数内部先打印全局age，再创建局部age = 20，再次打印age。
age=18
def func_9():
    global age
    print(age)
    age=30
    print(age)
func_9()
print(age)
# 题目10创建全局变量num = 10，
# 写两个函数：fun1：global 让num *= 2fun2：不使用global，新建局部num = 100依次调用两个函数，最后打印全局num
num=10
def func_10():
    global num
    num *= 2
def func_11():
    num = 100
# 依次调用两个函数
func_10()
func_11()
print(num)
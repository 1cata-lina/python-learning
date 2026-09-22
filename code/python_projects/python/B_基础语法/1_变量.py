'''
变量：用来存储数据的名字
定义：
变量名=值
命名规范
• 不能以数字开头
• 区分大小写
• 不能使用关键字
• 推荐使用小写字母+下划线
'''

name="zhangsan"
age=20
height=175.5
# print(name,age,height)
username,password="admin","123"
del username



'''
常用的内置函数：type(),int(),float(),str(),len()


'''
username="zhangsan"
password="pwd"
number="13356787667"
n="  123  "
#a=int(username)#❌ 报错，不能带字母
#b=int(password)
print(int(n))

status_code="200"
status_code=int(status_code)
if status_code==200:
    print("接口请求成功")

'''
\n:换行
\t:制表符
\":双引号
\':单引号
\\:反斜杠

'''
print("测试结果如下：\n1.选项一\n2.选项二\n3.选项三")

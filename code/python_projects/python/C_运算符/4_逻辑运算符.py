'''
逻辑运算符用于组合多个条件
• and：与
• or：或
• not：非

'''
from email import message

age=25
print(age>18 and age<60)
print(age<18 or age>=60)
print( not age ==30)

status_code=200
message="success"
if status_code==200 and message=="success":
    print("测试已经通过")
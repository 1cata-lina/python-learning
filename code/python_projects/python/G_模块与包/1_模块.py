# 一个 .py 文件就是一个模块。模块中可以包含变量、函数、类等内容。
# 使用模块可以：
# • 复用代码
# • 方便管理
# • 避免代码过长
'''方式1：导入整个模块'''
import math
print(math.sqrt(16))
'''方式2：导入指定成员'''
from math import sqrt
print(sqrt(25))
''' 方式3：导入全部成员'''
from math import *
print(sqrt(36))
'''方式4：取别名'''
import time as t
print(t.strftime("%Y-%m-%d"))

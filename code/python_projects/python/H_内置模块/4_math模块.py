'''
4. math 模块
知识说明
math 模块提供数学计算相关函数。
常用函数
• math.pi
• math.sqrt()
• math.pow()
• math.ceil()
• math.floor()
• math.fabs()
'''
import math

import math

# 1. math.pi —— 圆周率（一个固定的常量）
print(math.pi)        # 3.141592653589793
# 用处：算圆的面积 = π r²

# 2. math.sqrt(x) —— 平方根（谁乘自己等于 x）
print(math.sqrt(16))  # 4.0
print(math.sqrt(2))   # 1.4142135623730951
# 注意：结果是浮点数

# 3. math.pow(x, y) —— x 的 y 次方
print(math.pow(2, 3))  # 8.0（2的3次方）
print(math.pow(5, 2))  # 25.0
# 注意：结果永远是浮点数

# 4. math.ceil(x) —— 向上取整（往大数方向取）
print(math.ceil(3.2))   # 4   （3.2 → 最近的整数，向上是4）
print(math.ceil(3.0))   # 3
print(math.ceil(-3.2))  # -3  （负数向上是往0方向走）

# 5. math.floor(x) —— 向下取整（往小数方向取）
print(math.floor(3.8))  # 3   （3.8 → 向下是3）
print(math.floor(-3.2)) # -4  （负数向下是更小）

# 6. math.fabs(x) —— 绝对值（去掉负号）
print(math.fabs(-5))    # 5.0
print(math.fabs(3.7))   # 3.7
# 注意：结果永远是浮点数

'''
赋值运算符用于给变量重新赋值
常见的运算符：
• =
• +=
• -=
• *=
• /=
• %=
'''
count=0
count+=1
print(count)
count-=2
print(count)

minus=10
minus-=2
print(minus)
# 1. 超市会员初始余额money = 236，今日充值 84 元，使用+=更新余额并打印最终余额，写出结果。
money=236
money+=84
print(f"超市剩余余额{money}")
# 2. 用户水费账户原有余额water = 152，本月扣费 37 元，用-=计算剩余余额，输出答案。
water=152
water-=37
print(f"用户水费账号剩余费用{water}")
# 3. 单个笔记本售价price = 12，一次性采购 5 本，price *=5计算总价，输出结果。
price=12
price*=5
print(f"总共花了{price}去买笔记本")
# 4. 聚餐总花费total = 320，4 人 AA 平分，total /= 4，打印数值和数据类型。
total=320
total/=4
print(f"数据类型是{type(total)},聚餐总费用是{total}")
# 5. 一共 47 瓶可乐，每 6 瓶装一箱，用//=求能装满多少整箱。
coco=47
coco//=6
print(f"能装满多少箱{coco}")
# 6. 承接上题 47 瓶可乐，每 6 瓶一箱，%=计算装箱后剩余零散可乐数量。
coco%=6
print(f"装箱剩余可乐数量{coco}")
# 7. 本金固定系数rate = 2，存 3 年复利翻倍，rate **=3，输出运算结果。
rate=2
rate**=3
print(f"固定系数{rate}")
# 8. 用户姓name = "张"，拼接名字 "明"，使用+=实现字符串拼接，打印全名。
name = "张"
name+="明"
print(f"完整名称是{name}")
# 9. 表单录入：手机号前缀字符串tel = "138"，随机数字num=9966，代码res=tel+num，分析运行现象 + 报错原因。
tel = "138"
num="9966"
res=tel+num
print(res)
# 10. 单份套餐 29 元，活动：买 (2+1) 份套餐，food =29，food *= 2+1，计算总价。
food =29
food *= 2+1
print(food)#等号右边的所有运算都会优先执行完毕，然后再和左边的值进行乘法（或加法、减法等）。
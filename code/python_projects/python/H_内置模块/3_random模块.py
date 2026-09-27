'''random 模块用于生成随机数或随机选择数据• random.random()生成 [0,1) 之间的随机小数
• random.randint(a, b)生成  [a, b]  包含两端的随机整数
• random.randrange(start, stop, step)按步长取随机数，左闭右开
• random.uniform(a, b)a~b 之间随机小数
• random.choice(列表)随机抽取一个元素
• random.sample(列表, n)随机抽取 k 个不重复元素，返回列表
• random.shuffle(列表)原地打乱列表顺序，无返回值
• random.seed(x) 随机种子，固定种子，每次运行随机结果完全相同，用于复现数据
'''
import random

print(random.random())
print(random.randint(1, 100))

names = ["张三", "李四", "王五"]
print(random.choice(names))
print(random.sample(names, 2))


poker = [i for i in range(1,55)]
random.shuffle(poker)
print(poker)



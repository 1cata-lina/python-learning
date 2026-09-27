
# ==========  读取函数 ==========
def read_all(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

print(read_all("demo.txt"))
# ========== 写入函数 ==========
def write_lines(path, data_list):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(data_list)

write_lines("demo2.txt", ["hello\n", "python\n"])
# ========== 保存每日测试总结==========
def save_summary(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n")
save_summary("summary.txt", "2025-06-01：完成登录模块测试")
save_summary("summary.txt", "2025-06-01：发现2个缺陷")
# ================= 题目 1：三句话写入 + 读取输出 =================
with open("三句话.txt", "w", encoding="utf-8") as f:
    f.write("第一句：认真对待每一次测试，bug 会越来越少。\n")
    f.write("第二句：把复杂的问题拆成小步骤，就没有难题。\n")
    f.write("第三句：每天进步一点点，坚持带来大改变。\n")

with open("三句话.txt", "r", encoding="utf-8") as f:
    print("===== 三句话.txt 内容 =====")
    print(f.read())

# ================= 题目 2：一周食谱写入文件 =================
recipes = [
    "周一：早餐-鸡蛋三明治 午餐-鸡胸肉沙拉 晚餐-小米粥",
    "周二：早餐-燕麦牛奶 午餐-番茄牛肉面 晚餐-清蒸鱼+米饭",
    "周三：早餐-包子豆浆 午餐-木须肉盖饭 晚餐-蔬菜豆腐汤",
    "周四：早餐-煎蛋吐司 午餐-宫保鸡丁 晚餐-紫菜蛋花汤+馒头",
    "周五：早餐-香蕉酸奶 午餐-红烧排骨饭 晚餐-凉拌黄瓜+杂粮粥",
    "周六：早餐-蔬菜饼 午餐-火锅聚餐 晚餐-水果捞",
    "周日：早餐-牛奶麦片 午餐-家庭小炒 晚餐-饺子",
]
with open("一周食谱.txt", "w", encoding="utf-8") as f:
    for day in recipes:
        f.write(day + "\n")
print("===== 一周食谱.txt 已写入 7 天 =====")

# ================= 题目 3：商品列表写入文件 =================
goods = [
    ("苹果", 5.5, 10),
    ("香蕉", 3.2, 20),
    ("牛奶", 12.0, 5),
    ("面包", 8.0, 3),
]
with open("商品数据.txt", "w", encoding="utf-8") as f:
    for name, price, num in goods:
        f.write(f"{name},{price},{num}\n")    # 逗号分隔，方便下次解析
print("===== 商品数据.txt 已写入 4 条 =====")

# ================= 题目 4：读取用户账号文件并解析 =================
# 假设 user.txt 内容（每行：账号,密码,角色）：
# admin,123456,管理员
# test,001001,测试员
with open("user.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) < 2:              # 现在按 2 个字段校验
            print("跳过格式异常的行:", line)
            continue
        username = parts[0]
        password = parts[1]
        print(f"账号:{username} 密码:{password}")

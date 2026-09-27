'''读取文件'''
'''read()'''
with open("demo.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print("我是read()方法读取的文件内容：", data)
'''readline()'''
with open("demo.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print("我是readline()方法读取的文件内容：",line)

'''readlines()'''
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("我是readlines()方法读取的文件内容：",lines)
#思考如果不在同一个目录怎么办？：可以用方法把目录路径找到出来，然后拼接成完整的路径
# 案例：读取测试账号文件
with open("users.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    user_info = line.split(",")
    print(f"用户名：{user_info[0]}，密码：{user_info[1]}")
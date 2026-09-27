'''写入文件'''# 读取图片
with open("test.png", "rb") as f:
    img_data = f.read()

# 复制图片
with open("new.png", "wb") as f:
    f.write(img_data)
# write()
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
 # writelines()
data = ["登录通过\n", "注册通过\n", "支付失败\n"]
with open("report.txt", "w", encoding="utf-8") as f:
    f.writelines(data)
# 案例：写入测试执行结果
results = [
    "登录接口：通过\n",
    "用户查询接口：通过\n",
    "删除接口：失败\n"
]

with open("api_result.txt", "w", encoding="utf-8") as f:
    f.writelines(results)

print("测试结果写入完成")
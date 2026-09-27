import time

# 1. w 模式覆盖写入（文件不存在则创建，存在则清空重写）
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("第一轮功能测试完成")        # 写一行
# with 退出自动关闭文件

# 2. a 模式追加日志（不清空，续写末尾）
with open("result.txt", "a", encoding="utf-8") as f:
    f.write("\n本次执行1000次随机事件")   # 记得先补 \n 换行！
# 结果：第一行 + 第二行追加记录

# 3. write 分 3 次写入，每条换行
api_list = ['/login接口', '/register接口', '/user接口']
with open("api.txt", "w", encoding="utf-8") as f:
    for item in api_list:
        f.write(item + "\n")            # write 不自动换行，手动加 \n

# 4. writelines 列表批量写入
pkg_list = ["com.wechat", "com.tencent.mm", "com.qq"]
with open("blacklist.txt", "w", encoding="utf-8") as f:
    f.writelines(pkg + "\n" for pkg in pkg_list)   # 生成器补 \n
# 注意：writelines 不会自动加换行！列表元素里必须带 \n

# 5. with 上下文写入两行（自动关闭）
with open("user.txt", "w", encoding="utf-8") as f:
    f.write("账号：admin，密码123456\n")
    f.write("账号：test，密码：001001\n")

# 6. time 模块 + 追加 10 行，每行间隔 1 秒
with open("run_log.txt", "a", encoding="utf-8") as f:
    for i in range(10):
        f.write(f"测试时间:{time.strftime('%Y-%m-%d %H:%M:%S')} 状态:正常\n")
        time.sleep(1)                    # 停 1 秒再写下一行

# 7. 读 adb 日志筛选 com 行 → 写入新文件
with open("adb_log.txt", "r", encoding="utf-8") as f1, \
     open("com_log.txt", "w", encoding="utf-8") as f2:
    for line in f1:
        if "com" in line:                # 筛选包含 com 的行
            f2.write(line)               # 原样写入（保留原换行）

# 8. rb 读 + wb 写 → 复制图片
with open("screen1.png", "rb") as f1, \
     open("screen_copy.png", "wb") as f2:
    f2.write(f1.read())                  # 字节数据完整写入
print("图片复制完成")

# 9. r+ 模式在文件末尾插入一行
with open("tip.txt", "r+", encoding="utf-8") as f:
    f.seek(0, 2)                         # 2=文件末尾，光标移到结尾
    f.write("\n检查时间：2026年XX月XX日 时:分:秒\n")
# 关键：r+ 打开时光标在开头，直接 write 会覆盖开头，必须先 seek 到末尾

# 10. w 清空 → 写 10 条用例 → 统计行数
with open("temp.txt", "w", encoding="utf-8") as f:    # w 模式天然清空
    for i in range(1, 11):
        f.write(f"用例编号:TC{i:03d} 用例标题:登录测试{i} 前置条件:已安装APP "
                f"操作步骤:输入账号密码点击登录 预期结果:登录成功\n")
with open("temp.txt", "r", encoding="utf-8") as f:
    total = sum(1 for line in f)         # 逐行计数
print(f"temp.txt 共 {total} 行")

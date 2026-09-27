import re
# Python内置，无需pip安装
'''二、核心匹配函数
1. re.match()
从字符串开头匹配，只匹配首部'''
res = re.match(r'hello', 'hello123')
print(res.group())  # hello
# 开头不匹配返回None
print(re.match(r'123', 'hello123'))  # None
'''re.search() 全局查找，找到第一个匹配项'''
res = re.search(r'\d+', 'abc666def888')
print(res.group()) # 666
'''3. re.findall()
全局匹配，返回所有匹配结果列表（最常用）'''
res = re.findall(r'\d+', 'abc666def888')
print(res) # ['666', '888']
'''4. re.finditer()
返回迭代器，适合大量匹配节省内存'''
it = re.finditer(r'\d+', 'a1b2c3')
for i in it:
    print(i.group())
    '''re.sub() 替换（日志清洗高频）'''
    # 把数字替换成#
    s = "error 404 timeout 500"
    new_s = re.sub(r'\d+', '#', s)
    print(new_s)  # error # timeout #

    # 限定替换次数 count=1
    new_s2 = re.sub(r'\d+', '#', s, count=1)
    print(new_s2)  # error # timeout 500
    re.split()
    # 正则分割
    s = "user1,user2;user3 user4"
    res = re.split(r'[,; ]', s)
    print(res)  # ['user1', 'user2'# , 'user3', 'user4']
    '''三、元字符基础匹配规则
.  任意单个字符（除换行）
\d  数字 0-9
\D  非数字
\w  字母、数字、下划线、汉字
\W  非字母数字汉字下划线
\s  空格、制表、换行
\S  非空白字符
^  匹配字符串开头
$  匹配字符串结尾
四、数量限定符
*  0次或多次
+  1次或多次
?  0次或1次
{n}  恰好n次
{n,}  至少n次
{n,m}  n~m次'''
    # 匹配手机号11位数字
    phone = re.findall(r'\d{11}', "13800138000 abc12345678901")
    print(phone)  # ['13800138000', '12345678901']
    '''五、分组 () 提取指定内容
括号内内容单独捕获，用 group(1) 获取'''
    s = "status=200 code=503"
    res = re.search(r'status=(\d+)', s)
    print(res.group(1))  # 200
    '''六、预编译正则 re.compile()
重复使用同一规则时编译，提升效率'''
    # 编译匹配数字规则
    pat = re.compile(r'\d+')
    print(pat.findall("a1b2c3"))
    print(pat.search("test666").group())
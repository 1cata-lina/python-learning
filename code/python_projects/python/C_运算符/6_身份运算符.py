'''
成员运算符用于判断一个元素是否存在于某个容器中。
• in
• not in
'''
a=[1,2,3]
if 1 in a:
    print("1在集合内")

response_key=["code","message","data"]
if "code" in response_key:
    print("返回结果包含code字段")
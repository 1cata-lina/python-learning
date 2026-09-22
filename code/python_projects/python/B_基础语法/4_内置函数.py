'''

type()、int()、float()、str()、len()

'''
sun="yang光"
print(type(sun))
#a=int(username)#❌ 报错，不能带字母
#b=int(password)


status_code="200"
status_code=int(status_code)
if status_code==200:
    print("接口请求成功")
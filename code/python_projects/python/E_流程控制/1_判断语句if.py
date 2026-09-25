'''
判断语句用于根据条件是否成立执行不同代码。
单分支/双分支/多分支/嵌套判断/三元运算符'''
# 单分支
score = 58
if score < 60:
    print("成绩不及格")
# 双分支
score = 75
if score < 60:
    print("不及格")
else:
    print("及格")
# 多分支
score = 88
if score < 60:
    print("不及格")
elif score < 80:
    print("良好")
elif score <= 100:
    print("优秀")
else:
    print("分数有误")
# 嵌套判断
score = 95
if 0 <= score <= 100:
    if score < 60:
        print("不及格")
    elif score < 80:
        print("良好")
    else:
        print("优秀")
else:
    print("请输入正确成绩")
 # 三元运算符
num = 10
result = "偶数" if num % 2 == 0 else "奇数"
print(result)
'''一、布尔值（最基础）
 
二、数字类型
假值（False）： 0、0.0
真值（True）：所有非0数字

三、字符串 str
假值：空字符串  "" 
真值：任意非空字符串（包括  "0" 、 " "  空格）

四、容器类型（列表、元组、字典、集合）
假值：空容器  [] () {} set() 
真值：有元素的容器
 
五、None
 None  永远为假
 `0、0.0、""、[]、()、{}、set()`


1. 数字：0 和 0.0
2. 字符串：空字符串 `""`（⚠️带空格 `" "` 不算！）
3. 容器：空列表、空元组、空字典、空集合

> 
> 口诀（好读，默念几遍）
> **零、空串、空容器，除此以外全是真**
六、比较运算（最常用）
 > < >= <= == != 
 
七、逻辑运算 and / or / not
 
八、成员运算 in / not in
 
九、身份运算 is / is not'''
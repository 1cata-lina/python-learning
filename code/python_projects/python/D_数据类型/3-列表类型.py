'''
列表可以存储多个元素，元素类型可以不同，且支持增删改查。
有序、可变、可重复，容器型数据，能存放任意数据类型
支持索引(下标)、切片、增删改查
'''
name=["一","二","三"]
nums=[1,2,3,4,5,6,7,8,9]
mix=["admin",18,True]
#查找元素
print(name[0])
print(name[-1])
print(mix[0:2])
# 修改元素
nums[2]=4
print(nums)
# 添加新元素
users = ["admin", "test01"]
# 接把你给的东西，整体当成1 个整体，放到列表最后。
users.append("test02")
users.append(["test03","test04"])
#['admin', 'test01', 'test02', ['test03', 'test04']]
users.extend("test02")
#['test03', 'test04'], 't', 'e', 's', 't', '0', '2',
# 会把传入的序列拆开，把里面每一项，逐个加到列表末尾。
users.extend(["test03","test04"])
print(users)
# 't', 'e', 's', 't', '0', '2', 'test03', 'test04']
# insert () 指定位置插入
users.insert(0,"test05")
print(users)
users.insert(-1,111)
#加在最后一个的前面
# users.insert(len(users), "xxx")
users.insert(20, "xxx")
# insert 发现索引 3 不存在，直接把 xxx 放到最后面。下标≥列表长度 → 直接加到末尾
print(users)
# 删除元素
# del\pop()\remove()\clear()
nums=[1,2,3,4,5,6,7,8,9]
del(nums[0])
print(nums)
del nums[0]
print(nums)
res=nums.pop()
print(res)
## pop ()：按下标删除，**会返回删掉的值**
# - 不传参数：默认删除**最后一个元素**，并返回它
# - 传下标：删除指定下标元素，返回被删内容
print(nums)
# nums.remove(20)
##3. remove ()：按**元素内容**删除，不是下标
# 删除找到的**第一个匹配**的元素
# ⚠️ 如果这个元素不存在，直接报错！
print(nums)
nums.clear()
print(nums)

'''
列表常用函数和方法
len()/max()/min()/sum()/sort()/
reverse()/count()/index()过去元素的索引
count 是统计元素出现次数，找不到返回 0；index 是查找元素，
返回第一个匹配的下标，如果找不到元素会报错。

'''
nums = [5, 3, 9, 1, 5]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(nums.count(5))
print(nums.index(5))
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
'''
    sort()	             sorted()
类型	列表方法	         内置函数
原对象	直接修改原列表	不修改，返回新列表
返回值	None	         排序后的新列表
适用范围	只能列表	       列表、元组、字符串等可迭代对象

'''
a=[6,9,3,5,2,8]
print(a.sort())
print(a)
lst=[3,9,2]
lst_1=sorted(lst,reverse=True)
print(lst_1)


'''列表赋值，浅拷贝，深拷贝
copy.copy()
copy.deepcopy()'''
# 7.租房账单（新替换），浅拷贝修改内层水电费为150，查看原列表变化
bill = [1200, 300, ["水电", 180]]
# 浅拷贝特点：**第一层新开辟空间，嵌套的子列表还是共用同一个**，修改内层，原列表跟着变。
c1=bill.copy()# 列表.copy() 是浅拷贝，内置方法
c1[2][1]=150
print(c1)
print(bill)
# 8.员工信息深拷贝，deepcopy深拷贝，修改内层岗
import copy
# 正确写法：copy.deepcopy(对象)
# c2=emp.deepcopy()这是错误写法
emp = ["小明", 22, ["销售", "客服"]]
c2=copy.deepcopy(emp)
c2[2][1]="内层岗"
print(c2)
print(emp)
'''

1. 浅拷贝 `.copy()`：只复制第一层，嵌套列表共用。修改内层，原列表会变。
2. 深拷贝 `copy.deepcopy()`：递归复制所有层，全部独立互不干扰，**需要 import copy**。

'''
# 查饼干下标、删除第一个饼干
snack = ['薯片','饼干','果冻','饼干']
snack.remove('饼干')
print(snack)
print(snack.index('饼干'))
# ，合并列表求和
water=[25,32,18]
ele=[89,65,42]
water.extend(ele)
print(water)
print(sum(water))



'''
# Python列表常用方法汇总
## 一、增
|方法|作用|重点&坑点|
| ---- | ---- | ---- |
|append(元素)|在列表**末尾**添加1个元素|整体添加，不会拆分；原地修改，无返回值|
|extend(可迭代对象)|把里面元素逐个追加到列表末尾|拆分内容；`extend("abc")`会拆成a,b,c|
|insert(下标,元素)|在指定下标位置插入元素|`insert(-1, x)`插到倒数第一个**前面**<br>下标≥列表长度，自动加到末尾|

## 二、删
|方法|作用|重点&坑点|
| ---- | ---- | ---- |
|del 列表[下标]|按下标删除元素，支持切片批量删|关键字，不是方法；无返回值；下标不存在报错|
|pop(下标)|按下标删除，**返回被删除的元素**|不传参数默认删除最后一个元素；下标不存在报错|
|remove(元素)|根据**元素内容**删除，删第一个匹配项|找不到元素直接报错，不会返回值|
|clear()|清空列表所有元素|列表变量还保留，变成空列表`[]`|

## 三、查
|方法|作用|重点&坑点|
| ---- | ---- | ---- |
|index(元素)|查找元素，返回**第一个匹配**的下标|找不到元素直接报错，可以指定起始查找位置|
|count(元素)|统计元素在列表出现次数|找不到返回0，不会报错|

## 四、排序
|方法|作用|重点&坑点|
| ---- | ---- | ---- |
|sort()|列表方法，原地排序，修改原列表|返回值是None；`sort(reverse=True)`降序，**只能列表用**|
|sorted(对象)|内置函数，返回新的排序列表|**不修改原数据**；列表、元组、字符串都支持；`sorted(xxx,reverse=True)`降序|

## 五、其他
1. `reverse()`：原地反转列表顺序，直接修改原列表，无返回值
```python
lst = [1,2,3]
lst.reverse()
print(lst) # [3,2,1]




'''
'''
当某段代码需要重复执行且循环次数不确定时，适合使用 while。
while 条件:
    循环体
    break 和 continue
break：终止整个循环
continue：结束本次循环，进入下一次循环
'''
n = 1
while n <= 5:
    print("A")
    n += 1
# break：终止整个循环
n = 1
while n <= 10:
    if n == 5:
        break
    print(n)
    n += 1
# continue：结束本次循环，进入下一次循环
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# while...else如果循环正常结束，会执行 else；如果中途 break，则不执行。
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("循环执行完毕")

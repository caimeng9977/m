"""
双for循环嵌套: 外层循环每循环一次, 内层循环循环所有次, 内层循环体执行 就是内外层循环次数的乘积
for i in 范围:     -- 循环9次
    for j in 范围:    -- 循环9次
        循环体
"""
# 1. 双for
for x in range(3):
    for y in range(3):
        print("%d %d" % (x, y))
    print("这个属于外层循环的")
# 例: 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i} x {j} = {i*j}", end="\t")
    print("")
"""
while-for 循环嵌套使用
while 判断条件:
    for i in 范围:
        循环体
"""
# 例: 没有交作业, 如果每次没有交作业, 就说十遍我错了!, 三次机会, 结束
count = 0
while count < 3:
    print("猪八戒 没有交作业")
    for i in range(10):
        print("%d-我错了" % i)
    count += 1


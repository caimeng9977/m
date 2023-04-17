# 例1: 20以内说奇数不说偶数
for i in range(1, 21):
    if i % 2 == 0:
        print("过")
        continue
    print(i)
# 上边例子, 当我们遇到13就跳过
for i in range(1, 21):
    if i == 13:
        continue
    if i % 2 == 0:
        print("过")
        continue
    print(i)
# 例2: 回文数字, 比如四位数字 5665, 具有对称结构, 找出1000-9999中所有的回文数 1111, 2222, 2112
for number in range(1000, 10000):
    g = number % 10     # 取个位数
    q = number // 1000  # 取千位数
    b = number // 100 % 10  # 取百位
    s = number % 100 // 10  # 取十位
    if g == q and b == s:
        print(number)
# 练习: 斐波那契数列, 第一项 1  第二项 1
# 第三项 1 + 1 = 2
# 1 1 2  3  5  8 ....   算出一百项
a = 1
b = 1
for i in range(100):
    a = b
    b = a + b
    print(b)
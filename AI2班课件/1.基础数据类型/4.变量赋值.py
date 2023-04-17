# 变量赋值

# 1. 给单个变量进行赋值, 使用 = :赋值符号
# == : 判断左右两边相等
str_name = "天王星, 海王星, 冥王星"
print(str_name)
number = 888888888888888888
print(number)
pi = 3.1415926
print(pi)
bl = True
print(bl, type(bl))
# 2. 多个变量赋值相同的值
a = 10
b = 10
c = 10
# 使用连等号
x = y = z = 100
print(x, y, z)
# 3. 多个变量赋值不同的值
o = 6
p = 7
q = 8
# 左右两边一一对应赋值
n, m = 8000, 9000
print(n, m)
# 4. 两个变量交换数据
zhang = "宝马"
wang = "比亚迪"
print(zhang, wang)
# 可以利用第三个变量
zj = zhang  # zj = zhang = "宝马"
print(zj)
# wang = zj   # wang = zj ="宝马"
# zhang = wang    # zhang = wang = "宝马"
# print(zhang, wang)
zhang = wang    # zhang = wang = "比亚迪"
wang = zj   # wang = zj = "宝马"
print(zhang, wang)
# python中提供
zhang, wang = wang, zhang
print(zhang, wang)
# q = "貂蝉"  w = "昭君" r = "甄姬"
# 交换数据, q = "昭君", r = "貂蝉", q = "甄姬"

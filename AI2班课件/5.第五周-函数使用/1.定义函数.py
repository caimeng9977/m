"""
内置函数：print()，type()，id()，int()，len()，str()，bool()，float()，sum()，max()，min()...
函数：实现某些功能，将实现功能的代码封装起来
自定义函数：函数相当于爆米花的炉子，参数相当于玉米粒，糖，油，返回值(return)相当于爆米花
def：定义函数的关键字，
def 函数名(参数)：          -函数名，参数放入括号中
    函数体                  -函数体必须缩进在函数中
    return                  -返回值
函数名()                    -调用函数
函数名命名规则：字母数字下划线，不能数字开头，不能与关键字冲突，不与内置函数冲突，见名知意
"""
# 1. 定义函数，实现输出
def pt():
    print("迈克尔-杰克逊，I LOVE YOU!!!")
# 调用函数
pt()
pt()
# 2. 计算123456+98765
def jisuan():
    print(123456+98765)
jisuan()
# 3. 函数内定义变量
def chengfa():
    a = 100
    b = 856
    print(a * b)
chengfa()
# 4. 函数循环列表
def forlist():
    list1 = [1, 2, 3, 4, 5]
    for l in list1:
        print(l)
forlist()
# 5.判断星期
def week():
    x = input("输入汉字星期(聪明的人不乱写)：")
    if x == "星期一":
        print("Today is Monday")
    elif x == "星期二":
        print("Today is Tuesday")
    elif x == "星期三":
        print("Today is Wednesday")
    elif x == "星期四":
        print("Today is Thursday")
    elif x == "星期五":
        print("Today is Friday")
    else:
        print("Today is Weekend")
week()
# 练习1：使用函数打印乘法表，10 x 10 乘法表
def cfb():
    for x in range(1, 11):
        for y in range(1, x+1):
            print(f"{x} x {y} = {x * y}", end="\t")
        print(" ")
cfb()
# 练习2：判断字符串，输入一个字母判断，输出该首字母对应的星期/月份英文
n = []
def sx():
    k = int(input("请输入一个数字："))
    for x in range(100, 1000):
        bw = x // 100
        sw = x // 10 % 10
        gw = x % 10
        if x == bw ** 3 + sw ** 3 + gw ** 3:
            n.append(x)
    if k in n:
        print("正确")
    else:
        print("错误")
sx()


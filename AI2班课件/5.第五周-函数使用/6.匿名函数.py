"""
匿名函数(虚函数)：不需要命名，一般只使用一次，简化定义函数的代码，使用lambda关键字定义，可以使用参数，返回值，可以集合判断，不结合循环
def 函数名()
"""
# 1.输出函数
def say():
    print("这个是传统函数")
# ():起作用是执行这个函数
say()
print(say)
# 匿名实现
res = lambda : print("这个是匿名函数")
res()
# 2.添加参数
res2 = lambda x: print(x ** 10)
res2(10)
res22 = lambda x,y: print(x * y)
res22(4, 5)
# 3.传入序列，
res3 = lambda dict1: print(dict1["name"])
res3({"name":"吴老狗"})
# 4.结合判读,添加返回值
res4 = lambda name: "我爱中国" if name=="周恩来"else name
n = res4("周恩来")
print(n)
res44 = lambda score:"及格"if score >= 66 else "不及格"
print(res44(66))
# 练习1：判读一个数字是否为负值，是负数返回True，不是返会False
# 练习2：判断列表长度，如果是空列表，返回"空"，不是空列表，返回列表第一个值
res5 = lambda num: "True" if num < 0 else "False"
print(res5(2))
res6 = lambda list1: "空" if list1==[] else"非空"
print(res6(list1=[]))






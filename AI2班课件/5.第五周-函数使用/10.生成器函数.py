def demo(number):
    list1 = [i for i in range(1, 10)]
    list2 = []
    for i in list1:
        res = number * i
        list2.append(res)
        # 执行return,函数结束
    return list2
res = demo(10)
print(res)
# 使用生成器函数，一个个返回；使用yield返回，不使用return返回
# 取值会出现取出一个值，生成器中少一个值
def demog(number):
    list1 = [i for i in range(10)]
    for i in list1:
        res = number*i
        yield res
res = demog(10)
print(next(res))
print(next(res))
print(next(res))
print("---", next(res))
for r in res:
    print(r)
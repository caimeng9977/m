"""列表的更新, 更改列表的数据"""
list1 = ["天蓬元帅", "猪刚鬣", "猪悟能"]
# 修改列表的元素, 可以通过索引来修改所对应的元素; 列表名[索引] = 元素
print(list1[0])
list1[0] = "卷帘大将"
print(list1)
list1[-1] = "沙悟净"
print(list1)
"""python的内置函数, 可以操作列表"""
list2 = ["红楼梦", "西游记", "水浒传", "三国演义", "儒林外史", "聊斋志异"]
# 1. len(): 计算列表长度
print(len(list2))
# 2. str(): 将列表转换成字符串
print(type(list2))  # <class 'list'>
slist = str(list2)
# '["红楼梦", "西游记", "水浒传", "三国演义", "儒林外史", "聊斋志异"]'
print(slist, type(slist))   # <class 'str'>
# 3. sum(): 计算元素的和, 元素都是数值类型
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# res3 = sum(list2)
# print(res3)
numlist = [1, 11, 10, 2, 9.1]
res3 = sum(numlist)
print(res3)
# 4. max(): 计算最大值, 返回列表中最大的元素
print(max(numlist))
# 5. min(): 计算最小值, 返回列表中最小的元素
print(min(numlist))
# 6. sorted(): 对列表进行排序, 默认升序排列
res6 = sorted(numlist)
print(res6)
# 7. reversed(): 倒置列表, 放入列表会返回一个生成器, 需要用list()函数转换成列表
# <list_reverseiterator object at 0x0000019E6D1CAF60>
res7 = reversed(numlist)
print(list(res7))
# 8. list(): 可以将其他数据转换成列表, 字符串中每个元素都被转换成列表中单个元素
string = "金木水火土"
list8 = list(string)
print(list8)
# 9.enumerate(): 将列表进行遍历, 拿出 索引 和对应的值,
list9 = ["卡卡西", "卡卡罗特", "虹猫", "蓝猫", "问天"]
for index, value in enumerate(list9):
    print(index, value)

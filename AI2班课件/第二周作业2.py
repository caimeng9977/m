# 1.
"""
1. index(value, start, end): 获取元素在列表中首次出现的索引, value要查询索引的元素, start开始查找的索引位置, end结束的位置
2. count(): 查询元素出现的次数, 如果计算的元素不在列表中结果为0
3. sort(reverse=False): 排序, 默认为False升序排列, True降序排列
4.append(): 添加元素, 将元素添加到列表末尾
5.insert(index, 元素): 在列表的指定索引位置插入元素, 索引后边的元素对应的索引 + 1
6.extend(): 合并两个列表, 括号中放入列表, 所有元素有序添加进另一个列表
7.pop(): 默认删除最后一个元素, 可以通过元素索引进行删除
8.remove(): 直接移除元素, 当有多个元素重复时, 移除元素
9.reserve(): 列表倒置
10.clear(): 可以将列表清空, 变成空列表
11.copy(): 复制一个列表, 数据完全一样, 但是内存地址不一样, 不是同一个列表
12.关键字: del:删除列表
"""
# 2
result = 0
i = 0
while i <= 100:
    print(i)
    result += i
    i += 1
    print("输出1-100de累计和 = %d" % result)

# 3
num = int(input('请输入一个奇数数字:'))
for i in range(num, 0, -1):
    print(i*' '+(num+1-i)*'*'++(num-i)*'*')

# 4
ta = 49
lil = int(input("流量使用多少G："))
if lil <= 10:
    print("费用为49元")
elif 10 < lil <= 20:
    ta1 = (lil - 10) * 1 + ta
    print("花费使用金额为：", ta1)
elif 20 < lil <= 50:
    ta2 = ((lil - 20) * 2 + (lil - 10) * 1 + ta)
    print("话费金额为：", ta2)
elif lil > 50:
    ta3 = (lil - 50) * 5 + ((lil - 20) * 2 + (lil - 10) * 1 + ta)
    print("话费金额为：", ta3)


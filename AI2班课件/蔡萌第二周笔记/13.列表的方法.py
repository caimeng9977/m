"""方法,   列表名.方法 使用"""
list1 = ["熊大", "熊二", "光头强", "吉吉国王", "毛毛", "熊二", "光头强", "吉吉国王", "熊二", "光头强", "吉吉国王", "熊大", "熊二", "光头强"]
# 1. index(): 获取元素的索引, 当元素有多个取头一个元素的索引
x = list1.index("光头强")
print(x)
# 2. count(): 计算元素在列表的个数
c = list1.count("光头强")
print(c)
# 3. sort(): 对列表进行排序, 根据元素的编码进行排序, 默认列表升序排列(reverse=False), reverse=True 降序排列
list1.sort()
print(list1)
num_list = [89, 22, 23, 54]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
# 4. append(): 可以向列表中添加元素, 添加到末尾位置
list1.append("翠花")
print(list1)
list1.append("李老板")
print(list1)
# 5. insert(): 根据索引插入元素,
list5 = ["哪吒", "葫芦娃", "黑猫警长", "海尔兄弟"]
list5.insert(0, "中华小子")
print(list5)
list5.insert(3, "小福贵")
print(list5)
# 6. extend(): 将两个列表按照顺序进行合并元素
list6 = ["大头儿子", "图图", "花园宝宝"]
list6.extend(list5)
print(list6)
# 7. pop(): 删除元素, 默认删除最后一个, 可以根据索引删除对应的元素
list7 = ["海绵宝宝", "派大星", "章鱼哥", "蟹老板", "痞老板", "章鱼哥", "章鱼哥", "章鱼哥"]
list7.pop()
print(list7)
list7.pop(3)
print(list7)
# 8. remove(): 移除元素, 直接将对应元素移除, 有多个重复元素, 默认删除第一个
list8 = ["海绵宝宝", "派大星", "章鱼哥", "蟹老板", "痞老板", "章鱼哥", "章鱼哥", "章鱼哥"]
list8.remove("章鱼哥")
print(list8)
# 9.reverse(): 翻转列表
list8.reverse()
print(list8)
# 10.copy(): 克隆一个列表, 新的与旧的内存地址不一样, 不是同一个列表, 元素一样
newlist = list8.copy()
print(newlist)
print(id(list8), id(newlist))
blist = list8   # 给同一个列表再起一个名字
print(blist)
print(id(blist), id(list8))
# del  删除关键字
dlist = [1, 2, 3, 4]
del dlist[-1]
print(dlist)
del list8
# NameError: name 'list8' is not defined
# print("删除list8", list8)
# 11. clear(): 清空列表
dlist.clear()
print(dlist)

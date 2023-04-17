"""
字符串的方法: 字符串名.方法()
"""
# 1. index(): 获取子字符串的首字符的索引, 有多个重复取第一个
# 可以有起始位置, 终止位置(取不到); 当找不到时会报错
str1 = "To be or not to be , not not"
index1 = str1.index("not")
print(index1)
index2 = str1.index("o")
print(index2)
index3 = str1.index("o", 3, 10)
print(index3)
# index4 = str1.index("a")
# ValueError: substring not found
# print(index4)
# 2. find(): 与index()用法相同, 找不到不会报错, 会返回-1
str2 = "that is are question"
index4 = str2.find("are")
print(index4)
index5 = str2.find("a", 3, 9)
print(index5)
index6 = str2.find("l")
print(index6)
# 3. count(): 计算子字符串在原字符串中出现的个数
str3 = "年年岁岁花相似, 岁岁年年人不同"
print(str3.count("年"))
print(str3.count("岁岁"))
# 4. spilt(): 分割字符串, 返回一个列表, 当不填写参数, 默认分割空格, \t, \n等... 可以使用符号进行分割, 字符都行, 分割后, 用于分割的字符没有了, 每个的每部分都放入列表中, 可以指定分割的最大数
str4 = "明眸,皓#齿, 冰/肌@玉%骨, 娇小,可爱"
list1 = str4.split()
print(list1)
list2 = str4.split(",", 2)
print(list2)
# 5. strip(): 默认去掉首位的空格, 可以去掉字符串首位的字符
str5 = "a abc12 32.14 a"
print(str5)
print(str5.strip())
print(str5.strip("a"))
# 6. replace(): 替代
str6 = "飞流直下三千尺, 疑是银河落九天"
s1 = str6.replace("三", "9")
print(s1)
s2 = str6.replace("九", "33")
print(s2)
# 能不能直接修改字符串的内容, 例如列表修改元素
# TypeError: 'str' object does not support item assignment
# str6[0] = "跑"
# print(str6)
# 注意: 字符串的元素不能进行修改
# 7. upper(): 将小写转换成大写
str7 = "abcEFG"
print(str7.upper())
# 8. lower(): 将大写转换小写
str8 = "abcEFG"
print(str8.lower())

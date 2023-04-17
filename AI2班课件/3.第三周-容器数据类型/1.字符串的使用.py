"""基本数据类型：int, float, bool, str"""

"""字符串(str):是一个有序的容器类数据，有索引，与列表相同
str   "今天的天气真好"   字符串中每个字符都是一个元素
index 0,1,2,3,4,5,6
-index   -7-6-5-4-3-2-1
"""
# 1.字符串定义；空列表([], list(), 相当于False)
string = ""   # 相当于False
s = str()
print(s, type(s))
if string:
    print("真")
else:
    print("假")
s1 = "德玛西亚"
print(s1, len(s1))
# 2.字符串取值，同列表类似，也使用索引，字符串名[索引]
s2 = "学而时习之，不亦乐乎"
print(s2[3])
print(s2[-1])
print(s2[len(s2)-1])
# 3. 字符串切片， 和列表类似，左闭右开，右边取不到，其实位置不写默认为0索引，结束位置不写默认为字符串长度
# 步长：默认是1
print(s2[1:5])
print(s2[0:])
print(s2[:])
print(s2[1:9:2])
# 4.字符串相加，拼接字符串
a = "abc"
b = "123"
c = 789
print(a + b + str(c))
# 5.字符串乘数
print(a * 10)
print(b * 5)
# 6. 判断字符串中是否有某个字符串
str1 = "蜘蛛侠-pate-123"
if "蜘蛛" in str1:
    print("字符串中有蜘蛛")
if "0" not in str1:
    print("里面没有0")

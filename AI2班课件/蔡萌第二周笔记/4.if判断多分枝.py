"""
多分支结构是: 程序从上往下运行, 先进行第一个判断, 如果条件成立, 运行代码块1, 运行完结束, 如果不成功接着往下判断, 都不成立执行else的代码块
if 表达式1:
    代码块1
elif 表达式2:
    代码块2
elif 表达式3:
    代码块3
....
else:
    代码块
"""
# 例1: 0-59 评为 D, 60-79评为 C, 80-89 评为 B, 90-100评为A
score = input("请输入你的成绩: ")  # 字符串类型
score = float(score)
if 0 <= score < 60:
    print("评分为D")
elif 60 <= score < 80:
    print("评分为C")
elif 80 <= score < 90:
    print("评分为B")
elif 90 <= score <= 100:
    print("评分为A")
else:
    print("输入成绩不正确")
# 例2: 判断四季, 春天: 3, 4, 5  夏天: 6, 7, 8 秋天: 9, 10, 11 冬天: 12, 1, 2
month = int(input("请输入月份"))
if month == 3 or month == 4 or month == 5:
    print("春: 不知细叶谁裁出, 二月春风似剪刀")
elif month in [6, 7, 8]:
    print("夏: 小荷才露尖尖角, 早有蜻蜓立上头")
elif month in [9, 10, 11]:
    print("秋: 月落乌啼霜满天, 江枫渔火对愁眠")
elif month in [12, 1, 2]:
    print("冬: 黑狗身上白, 白狗身上肿")
else:
    print("地球上没有这个月份")
# 练习1: 定义变量 variable 随便给数据, 判断这个变量是什么数据类型
# 练习2: 定义变量 studay 周1-周5, 判断是周几, 然后输出专业课是那一节
studay = "周3"
print("专业课是第7, 8 节")

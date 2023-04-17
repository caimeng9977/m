"""
关键字参数：指定参数是什么，调用函数给参数传值
不定长参数：不确定参数有几个，可以传入多个参数,会打包成元组
不定长关键字参数：可以传入任意个关键字参数
"""
# 1.不定长参数，*去里面的数据
def func1(*args):
    print(*args)
    print(args, type(args))
# 调用函数，传入任意数据
func1(1, 2, 3, 4, 5)
# 例：传入多个参数，将参数写入到集合中进行去重
# print(*[1, 2, 3,])
# print(*[1, 2, 3])
print(*"abc")
def add_set(*num):

    # print(set(num))
    # ()定义空元组，[]定义列表，{}定义字典
    set1 = set()
    for n in num:
        set1.add(n)
        print(set1)
add_set("西施","昭君","貂蝉","玉环","昭君")
# 2. 不定长关键字参数
def func2(**kwargs):
    # print(**kwargs) # 不允许这样写
    print(kwargs,type(kwargs))
    print(kwargs["name"])
    for key,value in kwargs.items():
        print(key, value)
func2(name="秦始皇",xname="嬴政" )
# 例：传入学生的信息，拼接字符串输出
def stu_info(**students):
    name = students["name"]
    age = students["age"]
    sex = students["sex"]
    score = students["score"]
    string = ",".join([name, str(age), sex, str(score)])
    print(string)
stu_info(name="李四", age=19, sex="女", score=88)
# 练习1：使用不定长参数，传入数据，任意数据，需要数据判断，转化成字符串，然后输入后边 拼接--（数据类型）
def istype(*args):
    for date in args:
        tp = type(date)
        # isinstanve():参数1是数据，参数2是比较的数据类型，类型一致结果为True
        if isinstance(date, str):
            print(date + "--" + str(tp))
        elif tp == int:
            print(str(date) + "--" + str(tp))
        elif tp == float:
            print(str(date) + "--" + str(tp))
        elif tp == bool:
            print(str(date) + "--" + str(tp))
        else:
            # 传入的列表, 元组有数字需要转化字符串拼接
            if isinstance(date, list):
                data = [str(d) for d in date]
            elif isinstance(date, tuple):
                data = (str(d) for d in date)
            print(",".join(date) + "--" + str(tp))
istype(1, True, 3.56, "hello", [1, "a"], ("hi",))







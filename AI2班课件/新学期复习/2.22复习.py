
# 函数嵌套调用执行函数
# 自定义函数testB
def testB():
    print('---- testB start ----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end ----')
# 自定义函数testA
def testA():
    print('----- testA start ----')
    testB()
    print('---- testA end ----')
testA()

# 位置参数，调用函数时根据函数定义的参数位置来传递参数
def user_info(name,age,gender):
    print(f"你的名字是{name},年龄是{age},性别是{gender}")
user_info('TOM',20,'男')
# 注意：传递和定义参数的顺序及个数必须一致

# 关键字参数：函数调用，通过“键=值”形式加以指定
def user_info(name,age,gender):
    print(f"你的名字是{name},年龄是{age},性别是{gender}")
user_info('Rose',20,'女')
# 调用函数时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
user_info('小明',gender='男',age=16)

def user_info(name,age,gender='男'):
    print(f"你的名字是{name},年龄是{age},性别是{gender}")
user_info('Rose',18,'女')
# 调用函数时可不传该默认参数的值
user_info('TOM',20)

# 不定长参数
# 1. 动态位置传参
def user_info(*args):
    print(args)
user_info('TOM')
user_info('TOM',18)
# 2.动态关键字传参
def user_info(**kwargs):
    print(kwargs)
user_info(name='TOM',age=18,id=110)

# 按位置传参
def fun(a, b, c):  # 函数定义
    print("...")
fun(10, 20, 30)  # 函数调用，参数的顺序及个数要和定义时的参数保持一致

# 按关键字传参
def fun(a, b, c):  # 函数定义
    print("...")
    # 函数调用时，要用"="将关键字与值进行连接，此时，这三个参数表达式的位置可以换，因为编译器会根据关键字查找，然后再将值传递给形参
fun(a=10, b=20, c=30)
fun(b=12, c=14, a=8)

# 匿名函数
lst = [lambda x: x**2, lambda x: x**2, lambda x: x**2,]
for f in lst:
    print(f(9))
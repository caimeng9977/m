name = "张三"
age = 18
phone = 15136282191
def add(x, y):
    # __name__ 指的是当前文件名字
    print("{}模块的函数".format(__name__))
    return x + y
def odd(number):
    if number % 2 == 1:
        print(f"{number} 是奇数")
    else:
        print(f"{number} 是偶数")
class Student(object):
    pass
if __name__ == '__main':
    #  __name__获取当前文件的名字，__main__判断当前运行的环境是否与当前代码所在的文件一致
    print("执行模块!")
    print(f"{name}: {age}: {phone}")
    print(add(2, 3))
    odd(10)
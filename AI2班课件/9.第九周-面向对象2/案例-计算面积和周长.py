class Square(object):
    """计算正方的周长和面积"""

    def __init__(self,length):
        self.length = length

    def perimeter(self):
        """计算周长的方法"""
        p = self.length * 4
        return p

    def area(self):
        """计算面积的方法"""
        a = self.length ** 2
        return a
# 实例化对象，一个正方形
s = Square(length=10)
print(s.perimeter())    # 调用计算周长的方法
print(s.area())         # 调用计算面积的方法

# 练习：升级上边的案例，定义一个类可以计算出 长方形的周长和面积
class Square1(object):
    def __init__(self,chang,kuan):
        self.chang = chang
        self.kuan = kuan

    def zhouchang(self):
        b = self.chang*2 + self.kuan*2
        return b
    def mianji(self):
        c = self.chang * self.kuan
        return c
d = Square1(chang=10,kuan=5)
print(d.zhouchang())
print(d.mianji())

import math  # 数学模块
print(math.pi)

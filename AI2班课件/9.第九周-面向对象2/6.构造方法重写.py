# 构造方法继承重写
import math

class Triangle(object):

    def __init__(self, bottom_edge, height):
        # 本身就是函数，bottom_edge, height 是形参
        self.bedge = bottom_edge   # 给实例属性进行赋值
        self.height = height    # self.属性名   是最终对象的属性，类不能访问

    def v(self):
        self.name = "三角形"   # 只有在调用v方法时候才会产生name属性
        return  "%.2f" % (self.bedge * self.height * 0.5)

class ZTriangle(Triangle):

    # def __int__(self, bottom_edge, height):
    #      # 不建议这些重写init构造方法
    #     self.bedge = bottom_edge
    #     self.height = height
    def __init__(self, bottom_edge, height, bianchang):
        # 继承父亲实例属性
        # Triangle.__init__(self, bottom_edge, height)  #1.使用父类名调用构造方法
        super().__init__(bottom_edge, height)   # 使用super()调用父类的构造方法，不需要传入self参数
        self.bianchang = bianchang  # 子类在重写父类构造方法时新添加了属性
        # self.bedge = None    # 子类重写了父类的实例属性
        # self.height = None

    def v(self):
        height = math.sqrt(self.bianchang ** 2 - (0.5*self.bianchang) ** 2)
        return f"{self.bianchang * height * 0.5: .2f}"
# 实例化正三角形对象
zt = ZTriangle(bottom_edge=10, height=6, bianchang=90)  # 子类继承了父类的构造方法
# print(zt.name)   # 实例化对象，这个name属性并没有出现
print(zt.v())   # 调用计算面积函数，过程产生了一个name属性
# print(zt.name)
"""
练习1：定义类，解决鸡兔同笼问题，需要判断传入的数据是否正确
"""
class JT(object):
    flag = False
    def __init__(self, head: int, foot: int):
        if head > 0 and foot % 2 == 0:
            if head * 2 <= foot <= head*4:
                self.head = head
                self.foot = foot
                self.flag = True
            else:
                print("输入的脚数量不合理")
        else:
            print("输入的头数或脚数不合理")

    def get_jt(self):
        if self.flag:
            for t in range(0, self.head+1):
                j = self.head - t
                if t * 4 + j * 2 == self.foot:
                    return j, t
        else:
            print("请输入合理数据")
jt = JT(head=90, foot=80)
print(jt.get_jt())


"""父类：计算正方形面积与周长，定义属性为边长
子类：计算长方体表面积和体积，重写父类的构造方法
"""
class Sc(object):

    def __init__(self, bc):
        self.bc = bc
    def S(self):
        s = self.bc * self.bc        # 面积
        return s
    def C(self):
        c = self.bc * 4
        return c

x = Sc(bc=6)
print(x.S())
print(x.C())


class Cft(Sc):
    def __init__(self, chang, kuan, gao):
        self.chang = chang
        self.kuan = kuan
        self.gao = gao
    def Sb(self):
        b = (self.chang * self.kuan + self.chang * self.gao + self.kuan * self.gao) * 2
        return b
    def St(self):
        q = a = self.chang * self.kuan * self.gao
        return q
m = Cft(chang=10, kuan=2, gao=8)
print(m.Sb())
print(m.St())

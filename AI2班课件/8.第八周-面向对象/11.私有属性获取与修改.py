# 定义类
class Seafood(object):
    # 封装：将属性与方法进行保护不对外界暴露

    def __init__(self, name, sex, work, job):
        self.name = name     # 共有属性
        self.sex = sex
        self._work = work    # 保护属性
        self.__job = job     # 私有属性，类外访问不到，类内可以调用，

    def get_hidden(self):
        """获取私有属性的方法"""
        return self.__job

    def  set_hidden(self, job):
        """修改属性的方法"""
        self.__job = job

if __name__ == '__main__':
    baobao = Seafood(name="海绵宝宝", sex="男", work="厨师", job="抓水母")
    print(f"{baobao.name}是{baobao.sex}孩子,职业{baobao._work}")
    # 通过调用获取私有属性的方法来查看私有属性
    j = baobao.get_hidden()
    print(f"{baobao.name}是{baobao.sex}孩子,职业{baobao._work}, 爱好{j}")
    # 再实例化一个章鱼哥
    zyg = Seafood(name="章鱼哥", sex="男", work="收银员", job="吹笛子")
    print(f"{zyg.name}是{zyg.sex}孩子,职业{zyg._work}, 爱好{zyg.get_hidden()}")
    # 修改私有属性，通过修改私有属性方法进行修改
    zyg.set_hidden(job = "弹钢琴")
    print(f"{zyg.name}是{zyg.sex}孩子,职业{zyg._work}, 爱好{zyg.get_hidden()}")





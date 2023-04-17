# 继承：子类继承父类的属性和方法，子类实例对象可以调用父类的属性和方法，也可以继承后重写父类的属性和方法
# 单继承：子类继承一个父类
class Father(object):
    # object：所有的类继承于基类，给定义的类提供魔法方法
    # 类属性
    work = "伐木"
    _job = "抓熊"

    def day_work(self):
        print("砍树，伐木...")
    def _day_job(self):
        print("抓熊大，熊二")
class Son(Father):   # 继承一个父类，单继承
    # 子类继承父类
    hobby = "徒步"

    def study(self):
        print("学习开挖掘机...")
# 实例化对象
mao = Son()
print(mao.work, mao._job)     # 子类继承了父类的属性，可以实例化对象进行调用
mao.day_work()  # 子类继承了父类的方法，可以用实例对象进行调用
mao._day_job()
print(mao.hobby)   # 拥有自己的属性
mao.study()   # 自己方法

class GrandFather(object):   # 间接父类

    work = "土夫子"

    def ee(self):
        print("会打盗洞")   # 直接父类
class Father(GrandFather):

    job = "鉴别古董"
    def collect(self):
        print("收藏古董")
class Son(Father):

    hobby = "考古"
    def protect(self):
        print("保护文物...")

# 实例化
wuxie = Son()
print(wuxie.work,wuxie.job,wuxie.hobby)
wuxie.ee()  # 子类继承父类的父类方法，可以调用
wuxie.collect()
wuxie.protect()
class Father(object):

    work = "砌墙"
    __attr = "私有属性"   # 私有属性只有类内可以调用，不能被继承
    def day_work(self):
        print("去盖房子")

class Uncle(object):

    job = "刷墙"
    def day_job(self):
        print("刮大白...")

class Son(Father,Uncle):   # 继承多个父类，叫做多继承
    hobby = "房屋设计"
    def mywork(self):
        print("画图纸")
# 实例化
yangshilei = Son()
yangshilei.day_work()
yangshilei.day_job()
yangshilei.mywork()

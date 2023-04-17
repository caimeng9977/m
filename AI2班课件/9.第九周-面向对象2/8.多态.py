# 多态：指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数
class ArmyDog(object):

    def bite_enemy(self):
        print("追击罪犯")
class DrugDog(object):
    def track_drug(self):
        print("搜查毒品")
class Police(object):
    def army_work(self, dog):
        dog.bite_enemy()
    def drug_work(self,dog):
        dog.track_drug()
# 实例化一个警察
zhu = Police()
zhu.army_work(dog=ArmyDog())   # 实例化的对象调用方法，需要将实例化dog对象传入
zhu.drug_work(dog=DrugDog())   # 实现追查毒品
# 利用类的多态进行简写
class ArmyDog(object):

    def work(self):
        print("追击罪犯")
class DrugDog(object):
    def work(self):
        print("搜查毒品")
class Police(object):
    def work(self, dog):
        dog.work()
# 实例化一个警察
# 多态调用
sun = Police()
sun.work(dog=ArmyDog())  # 这个方法起到追击罪犯的作用
sun.work(dog=DrugDog())  # 这个方法起到搜查毒品的作用
"""练习：定义工具：抹布，拖把 可以有不同的方法，相同的方法名，定义学生类：有清洁方法，需要工具做参数写入，使用多态的写法"""
class Mabu(object):
    def work(self):
        print("擦玻璃")

class Tuoba(object):
    def work(self):
        print("拖地")
class Student(object):
    def work(self,tool):
        tool.work()
cai = Student()
cai.work(tool=Mabu())
cai.work(tool=Tuoba())





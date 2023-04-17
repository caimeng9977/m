# 定义一个类
# 类名：需要首字母大写，遵循大驼峰命名原则，当多个单词命名时首字母都大写
class Person:
    pass

# 首字母大写是规范，不是必要的要求
class dog:
    pass

# 创建学生类
class Student:
    pass
# 创建班级类
class Class:
    pass
# 创建人对象,创建对象的过程叫做实例化对象
zhangsan = Person()
# 创建学生
sunmingchen = Student()
# 查看类，查看对象
print(Student)  # <class '__main__.Student'>
print(sunmingchen)    # <__main__.Student object at 0x000001F43E6DBCC0>

class Boyfriend:
    pass
lishuguang = Boyfriend()
print(Boyfriend)
print(lishuguang)

class Sister:
    pass
cairuirui = Sister()
print(Sister)
print(cairuirui)

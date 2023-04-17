class Student(object):

    def __init__(self, id, name, sex, phone):
        self.id = id
        self.name = name
        self.sex = sex
        self.__phone = phone

    @property  # 将这个方法调用方式变成属性方式获取
    def phone(self):
        # 类的内部可以调用私有属性
        return  self.__phone
    @phone.setter  # 将修改属性方法变成属性进行修改的方式
    def phone(self, p):
        # 内部修改私有属性
        self.__phone = p

if __name__ == '__main__':
    sun = Student(id="1246678", name="孙铭晨", sex="男", phone="12345678998")
    # 通过方法获取修改私有属性变成属性进行修改的方式
    def phone(self, p):
        # 内部修改私有属性
        self.__phone = p

if __name__ == '__main__':
    sun = Student(id="1246678", name="孙铭晨", sex="男", phone="12345678998")
    # 通过方法获取私有属性
    # print(sun.get_hidden())
    # sun.set_hidden(p="18272511283")
    # print(sun.get_hidden())
    # 公有属性获取修改
    print(sun.name)
    sun.name = "孙明臣"
    print(sun.name)
    # 让方法变成属性调用方式
    cai = Student(id="456789", name="蔡萌", sex="女", phone="98745612300")
    print(cai.phone)
    cai.phone = "15093637989"
    print(cai.phone)


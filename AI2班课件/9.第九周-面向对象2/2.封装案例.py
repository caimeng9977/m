# 账号密码登陆验证
class Login(object):
    # 类属性
    __user = "root"
    __passwd = "123456"
    __userflag = False   # 表示验证user不通过
    def __init__(self, name):
        # 实例属性，实例化方法
        self.name = name
        print(f"欢迎{self.name}登陆账号")

    def yzuser(self, username):
        if username == self.__user:
            print("账号验证通过")
            self._userflag = True
        else:
            print("账号验证不通过")


    def yapasswd(self, password):
        if self._userflag:
            if password == self.__passwd:
                print("登陆成功...")
            else:
                print("登陆失败")
        else:
            print("请输入正确的账号， 先")

    def start(self):
        # 验证账号
        un = input("账号:")
        login0426.yzuser(username=un)
        # 验证密码
        pd = input("密码:")
        login0426.yzpasswd(passwd=pd)
# 增加新的功能，当我i们登陆验证密码3次，让登录和注册的功能进行锁定，不能使用
if __name__ == '__main__':
    # 测试一下
    login0426 = Login(name="蔡萌")
    login0426.start()


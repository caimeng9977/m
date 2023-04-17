def check_user(file_name="login.csv"):
    with open(file_name,"r", encoding="utf_8")as f:
        user_list = f.readlines()[1:]
        user_dict = {user.strip().split(",")[0]:user.strip().split(",")[1] for user in user_list}
        return user_dict
# 验证账号密码
count = 1
black_list = []
while count <= 3:
    user = input("账号:")
    if user in black_list:
        print("你已经被拉黑，请联系客服人员:151362821910")
        break
    while user not in check_user().keys():
        print("请输入账号，请重新输入")
        user = input("账号:")
    passwd =input("密码:")
    if passwd==check_user()[user]:
        print("登陆成功")
        break
    else:
        print("密码错误")
        if count == 3:
            black_list.append(user)
        else:
            count += 1
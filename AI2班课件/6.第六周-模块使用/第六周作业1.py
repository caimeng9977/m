# 1. 将考试的四道编程题写成代码运行无误后, 放一个py文件上交
"""
1)请写出一段Python代码实现输出99乘法表，根据需求写出部分代码逻辑结构，正确输出运行结果
2)请写出一段Python代码实现删除一个list里面的重复元素
3)苹果3元一个，鸭梨2元一个，桃子1元一个.现在想用200元买100个水果，请写出对应代码计算相应的组合，根据需求写出部分代码逻辑结构，正确输出运行结果
 4)模拟用户登录验证的，实现用户名输入，密码输入及验证等，用户在3次内输入正确密码登陆成功，连续输错3次密码登陆失败，且该用户被记录在黑名单，黑名单中的用户被锁定不能再登陆，根据需求写出部分代码逻辑结构，完整实现功能
"""
# 1)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} == {i*j}", end="\t")
        print("")
# 2)
list1 = ["嬛嬛", "大胖橘", "果子狸", "拽妃", "安小鸟", "大胖橘"]
set1 = set(list1)
print(set1)
# 3)
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            shuiguo = 3*i + 2*j + 1*k
            if shuiguo == 200 and i + j + k ==100:
                print(f"苹果{i}元一个,鸭梨{j}元一个,桃子{k}元一个")
# 4)

username = ["张三", "李四"]
passwd = [123456, 987654]
list2 = []
count = 0
while count <= 3:
    user = input("请输入您的账号: ")
    if user in list2:
        print("无法登录，账号已拉黑")
        break
    while user not in username:
        print("输入的账号不存在，请重新输入")
        user = input("请重新输入您的账号: ")
    pd = input("请输入您的密码: ")
    while pd in passwd:
        print("登陆成功")
        break
    else:
        print("密码错误")
        count += 1
        if count == 3:
            list2.append(user)

# 2. 使用匿名函数判断出传入一个字符串学号是否属于本班学生
res1 = lambda  id_class: "是本班学生" if 202115050201  <= id_class <= 202115050240 else "不是本班学生"
print(res1(202115050232))
# 3. 使用map函数, 传入一个列表, 将奇数与偶数分开
js = []
os = []
def num1(a):
    if a  % 2 == 0:
        os.append(a)
    else:
        js.append(a)
    return f"奇数:{js} 偶数:{os}"
b = map(num1, [1, 2, 3, 4, 5, 6])
jos = ""
for i in b:
    jos = i
print(jos)
# 4. 定义函数, 传入一个字典, 字典键为学生姓名, 值为学生成绩,返回值是成绩的最大值与最小值
def dict1(a):
    b = a.values()
    b1 = list(b)
    b1.sort()
    return print(f"最大值{b1[-1]}, 最小值{b1[0]}")
dict1({"lisa":99, "jennie":88, "rose":87})
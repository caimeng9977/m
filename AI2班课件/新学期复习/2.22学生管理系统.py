list=[]
def xs():
    print("""
    ----------菜单选择----------
    1.添加功能
    2.删除功能
    3.查询功能
    3.展示功能
    4.修改功能
    --------------------
    """)


def add():
    print("""----添加学生信息----""")
    name = input("输入姓名")
    age = int(input("输入年龄"))
    gender = input("输入性别")
    for i in list:
        if i['name'] == name and i['age'] == age and i['gender'] == gender:
            print('学生信息已存在')
            return
    dict1 = {}
    dict1['name'] = name
    dict1['age'] = age
    dict1['gender'] = gender
    list.append(dict1)
    print(list)



def delete():
    print('-------欢迎进入删除学生页面--------')
    num = int(input('请输入您要删除的序号'))
    if 0 <= num <= len(list)-1:
        delete_num = input('你确定要删除?(y/n)')
        if delete_num == 'y' or delete_num == 'yes':
            del list[num]
            print('删除成功')
        elif delete_num == 'n' or delete_num == 'no':
            print('退出删除操作')
            add()
    else:
        print('输入的序号错误，请重新操作')


def show():
    for i, j in enumerate(list):
        print('序号%d 姓名%s 年龄%d 性别%s' % (i,j['name'],j['age'],j['gender']))

def update():
    print('------欢迎进入学生修改页面------')
    show()
    print('------以上是所有学生信息------')
    num = int(input('请输入你要修改的学号'))
    if 0 <= num <= len(list) -1:
        list[num]["name"] = input('请输入你修改后的姓名')
        list[num]['age'] = int(input('请输入修改后的年龄'))
        list[num]['gender'] = input('请输入修改后的性别')
        print('修改成功')
        print('----以下是修改过后的学生信息----')
        print(list[num])
    else:
        print('请输入正确的学号')


def find():
    print('------欢迎进入查询学生页面------')
    name = input('请输入你要的姓名')
    for i in list:
        if i['name'] == name:
            print(i)
        else:
            print('该学生不存在')

def main():
    while True:
        xs()
        num = int(input('请输入需要的功能：'))
        if num == 1:
            add()
        elif num == 2:
            delete()
        elif num == 3:
            find()
        elif num == 4:
            show()
        elif num == 5:
            update()
if __name__ == '__main__':
    main()
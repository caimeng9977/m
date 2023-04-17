"""
csv文件：逗号分隔离
"""
f = open(file="学员信息.csv", mode="a+", encoding="utf-8")
# 学员姓名：性别：班级：成绩
f.write("孙悟空，公，菩提1班，99\n")
f.write("猪八戒，公，天庭1班，60\n")
# 写入列表
list_stu = ["沙悟净","男","流沙河班","59"]
# join():拼接字符串
f.write(",".join(list_stu))
# 移动光标
f.seek(0)
text = f.read()
print(text)
f.close()
""""

os模板：处理系统的目录
"""
import os
# os里面的变量
# 1.name:获取操作系统的名字，windows是nt,linux系统，Mac os是 posix
name = os.name
print(name)
# 2.linesep:获取系统的换行符；window,linux系统是" \n"
lp = os.linesep
print(lp)
# 3.sep:获取系统路径的分割符号，window,linux路径分割符号是\
#  C:\Users\蔡萌\Desktop\AI2班课件\6.第六周-模块使用
sep = os.sep
print(sep)
# os里面的函数
# 1.getcwd(): 获取当前工作环境的路径，类比linux的pwd命令
cwd = os.getcwd
print(cwd)
# 2.mkdir(): 创建一个空目录，如果目录存在会报错
# os.mkdir("abc")
# os.mkdir(path=r"C:\Users\蔡萌\Desktop\AI2班课件\6.第六周-模块使用\tools\新目录")
#  3.makedirs(): 创建多级目录，创建目录存在会报错
# os.makedirs("a/b/c")
# 4.chdir():切换当前工作环境的目录
os.chdir(r"C:\Users\蔡萌\Desktop\AI2班课件\1.基础数据类型")
cwd1 = os.getcwd()
print(cwd1)
# os.mkdir("第一周的目录")
# os.chdir(path=cwd)
# 5.rmdir():删除单个空目录，删除的目录如果找不到会报错
# os.rmdir("abc")
# 6. removedirs():删除多级目录，目录不存在会报错
# os.removedirs("a/b/c")
# 7.listdir(): 查看某个路径下边的文件和目录信息，返回一个列表，每个元素是文件和目录名字
cwd2 = os.getcwd()
ld = os.listdir(path=cwd2)
print(ld)
# 8.walk():遍历目录树，返回一个元组，有三个元素，路径名，目录列表，文件列表
res = os.walk(r"C:\Users")
print(res)
# for r in res:
#        print(r)
# 9. remove():删除指定文件，若不存在会报错
# os.remove("math.py")
# os.remove(r"C:\Users\蔡萌\Desktop\AI2班课件\test.py")
# 10.rename(): 重新命名文件或目录，新名字如果存在或报错
# os.rename("猜拳游戏.py","自定义游戏".py)
# os.rename("自定义游戏.py","猜拳游戏.py")
# 11.stat():返回文件的系统相关信息
res = os.stat("function_tools.py")
print(res)
# 12.copyfile():在shutil模块里的函数，复制文件
import shutil
shutil.copyfile("function_tools.py", "ft.py")


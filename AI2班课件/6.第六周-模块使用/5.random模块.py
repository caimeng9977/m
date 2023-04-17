"""
random模块：生成随机数，做随机选择使用
"""
import random
# 1. randint(a,b):产生一个[a, b]的随机整数
n = random.randint(1, 9)
print(n)
# 2.random():产生一个[0,1)之间的一个随机浮点数
f = random.random()
print(f)
# 3.randrange(start,stop,step):在[start, stop]之间以step步长产生一个随机数
res = random.randrange(0, 10, 2)  # 相当于在[0, 2, 4, 6, 8]
res1 = random.randrange(1, 10, 2)
print(res)
print(res1)
# 4.sample(list, k):在序列中随机取出k个元素，以列表形式返回
list1 = random.sample([1,2,3,4,5,6,7], k=3)
print(list1)
# 5.seed():改变随机生成器的种子，默认的参数是系统的时间
import time
print(time.time()) # 时间戳
# random.seed(0)
for i in range(10):
    print(random.randint(1, 9))
# 6. shuffle():打乱序列中的元素
card = [c for c in range(1, 11)]
card.extend(["J", "Q", "K"])
print(card)
random.shuffle(card)
print(card)
# 7.uniform(a,b):在[a,b]范围内产生随机浮点数
ff = random.uniform(1.23, 2.33333)
print(ff)
# 8.choice():从序列表随机选取一个元素返回
v = random.choice(["石头", "剪刀","布"])
print(v)
# 9.choice(sep, k):从序列中随机抽取多个元素放入列表返回
list2 = random.choices(range(10),k=2)
print(list2)
# 10. getrandbits(k):产生一个k比特长度的随机数
# 11 -- 3
# 100，111 -- 7
res10 = random.getrandbits(3)
print(res10)
# 练习(2分题): 生成随机的验证码, 可以定义生成验证码长度, 验证码包含, 数字与字母(区分大小写)
def yanzm(length):
    az = [chr(i) for i in range(65, 91)]
    AZ = [chr(j) for j in range(97, 123)]
    num = [str(n) for n in range(0, 10)]
    lt = az + AZ + num
    yan = ""
    for n in range(length):
        s = random.choice(lt)
        yan += s
    return yan
print(yanzm(4))

def zy():
    checkcode = ""
    for i in range(4):
        k = random.randint(0, 3)
        if k == i:
            b = chr(random.randint(65, 90))
        else:
            b = random.randint(0, 9)
        checkcode += str(b)
    print(checkcode)
# 定义类，在外部添加属性
class Hero:
    pass
# 实例化对象
daji = Hero()
# 添加属性，通过对象添加属性
daji.name = "妲己"
daji.occ = "法师"
daji.hp = 4600
daji.mp = 800
daji.attact = 180
# 利用对象调用属性
print(f"{daji.name}职业是{daji.occ}血量{daji.hp}魔法值{daji.mp}攻击力{daji.attact}")
# 2.定义类，添加类属性
class Boyfriend:
    # 定义类属性
    height = 180
    weiht = 130
    fule = "白色"
    job = "程序员"
    salary = 1000000
# 实例化对象，这个对象会带有类属性
bf1 = Boyfriend()
print(f"你的男朋友是{bf1.job}, 年薪{bf1.salary}")
bf2 = Boyfriend()
print(f"你的男朋友是{bf1.job}, 年薪{bf2.salary}")
bf2 = Boyfriend()
bf3 = Boyfriend()
# 1.通过类给类添加属性，这个属性会是类属性，所有实例化的对象都会拥有这个属性
Boyfriend.say = "I LOVE YOU"
bf4 = Boyfriend()
print(bf4.say)
print(bf1.say)
# 通过类调用属性
print(Boyfriend.height, Boyfriend.weiht)
# 2. 通过对象添加属性
huazi = Boyfriend()
huazi.sing = "会唱歌"
print(huazi.sing)
# print(bf1.sing)
# 类不能调用对象属性
# print(Boyferind.sing)


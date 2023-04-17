color_list = [
    ["红色", "大红色", "枫叶红", "复古红"],
    {"绿色": ["柳叶绿", "水绿色", "翠绿色"]},
    ("黄色", "浅黄色", "淡黄色"),
    "蓝色-天蓝色-瓦兰色"
]
# 对列表内进行取值，取出所有的值，一红绿蓝黄作为字典的键，其他同类颜色放入列表作为字典的值
# color_dict = {"红色": ["大红色", "枫叶红", "复古红"]}
color_dict = {}
for color in color_list:
    print(color)
    if type(color) == list:
        # 字典添加值
        color_dict[color[0]] = color[1:]
    elif type(color) == tuple:
        color_dict[color[0]] = list(color[1:])
    elif type(color) == dict:
        color_dict.update(color)
    elif type(color) == str:
        list1 = color.split("-")
        color_dict[list1[0]] = list1[1:]
    else:
        print("不考虑")
print(color_dict)
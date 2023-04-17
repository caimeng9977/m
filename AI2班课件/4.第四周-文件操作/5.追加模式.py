
"""a:追加写模式，打开文本，文本不存在会创建，不会清空文本，会接着文本的末尾写入，只会在末尾写入与光标无关"""
fa = open("水调歌头.txt", "a", encoding="utf-8")
print(fa.readable())  # 不可读
print(fa.writable())  # 可以写
fa.write("明月几时有，把酒问青天\n")
fa.seek(0)
fa.write("不知天上宫阙，今夕是何年\n")
fa.close()
"""a+:追加写读模式，打开文本，文本不存在会创建，不会清空文本，会接着文本的末尾写入，只会在末尾写入与光标无关"""
faj = open("临江仙.txt", "a+", encoding="utf-8")
print(faj.readable()) # 可读
print(faj.writable()) # 可写
faj.write("滚滚长江东逝水，浪花淘尽，是非成败转头空\n")
# 读取数据

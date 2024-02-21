#before = input("before: ")
#print("after: ", end="")
#for c in before:
#   print(c.upper(),end="") #python中默认自动分行所以自动end with“\n",如果不要自动，则加上这部分
#在上一行中，upper是每一个字符串附带的方法。
#所以可以将前两行修改为：
#print(before.upper())
#print() #这一行的目的在于让光标自动到下一行，啥也不打印。


#也可实现为
#before = input("before: ")
#after = before.upper()
#print(f"after:{after}") #在python中，在string前加入f则可以在该字符串内部使用{},print不会打印{}中的内容，而是打印插入花括号中的内容


#或者更简化
before = input("before: ")
print(f"after:{before.upper()}")
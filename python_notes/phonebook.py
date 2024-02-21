names = ["carter","david","john"]

name = input("name: ")
for n in names:
    if name == n:
        print("found")
        break
#可以将前五行简化为
#if name in names:
#    print("found")
else:
    print("not found")
#一般只有if和else的组合，但是在python中for函数也可以和else平级使用，即使for循环结束后，python自动知道
#与之对应的else语句。
        
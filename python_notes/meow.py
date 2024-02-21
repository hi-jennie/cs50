#def main():
#   for i in range(3):
#       meow()

#def meow():
#    print("meow")
    
#main()
#def 只是def ，def之后要调用函数才能运行，一般我们都是把
#主函数写在前面，所以可以用main函数将其框起来。



#修改——将循环也定义为具有普遍性的函数
def main():
    meow(7)
    
def meow(n):
    for i in range(n):
        print("meow")

main()
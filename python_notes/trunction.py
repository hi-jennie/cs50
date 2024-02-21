# x = int(input("x:  "))
# y = int(input("y:  "))

#z = x / y
#print(z)  在python中，小数点后面的位数不会被截断
#ps print(f"{z:.50f}")  表示打印小数点儿50位

#在python中不存在integer overflow




#识别错误的方法
def get_int(promt):
    while True:#在python中，true需要大些，表示一直循环
        try:
            return int(input(promt))
        except ValueError:
            print("Not an integer") #也可以改为pass
            
def main():
    x = get_int("x: ")
    y = get_int("y: ")
    
    print(x+y)

main()

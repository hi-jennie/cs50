from cs50 import get_int

while True:
    n = get_int("height")
    if n >0:
        break
    #当用户输入身高时 就会break并开启print，否则就会循环的get_int.
for i in range(n):
    print("#")
    
    
    
    #打横着的“#”
    #for i in range(4):
    #    print("#",end="")
    #print()
    
#以上三行也可以实现为
# print("#" * 4)
    
    
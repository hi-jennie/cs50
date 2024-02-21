k#s = input("Do you agree?")

#if s =="Y" or s == "y":
#    print("Agreed")
#elif s =="N" or s =="n":
#    print("Not agreed")
    
#要输入的y.yes,no,n都能执行命令则    
s = input("Do you agree?")
s = s.lower()#将输入的s转换为小写再执行
#或者将前两步合并s = input("Do you agree?").lower()
if s in ["y","yes"]:
    print("Agreed")
elif s in ["n","no"]:
    print("Not agreed")

from sys import argv

if len(argv) == 2:
    print(f"hello,{argv[1]}")
else:
    print("hellp,world") #跟c语言中一样，argv[0]实际上是文件的名字即greet.py
import csv

with open("favorite,csv","r") as file:
    #打开名为favorites.csv的文件为可读模式，并可以访问其中的字节，python可以自动关闭文件
    reader = csv.reader(file)
    #让python自带的函数帮我读取文件的逗号在哪儿，这样就可以逐行提供文件中的数据
    next(reader) #因为第一行是时间，语言所以就跳过，表明在reader这个变量中读取下一行
    for row in reader:
        print(row[1]) #这里的1其实就是第二行,执行的效果其实就是依次把每一行中的第二个参数打印出来，即打印第二列。
        #或者重新声明一个变量改为：favorite = row[1]
        #                      print(favorite)
    
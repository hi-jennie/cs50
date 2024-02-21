import csv

with open("favorite.csv","r") as file:
    reader = csv.DictReader(file)
    #不再跳过标题，因为dictreader可以自动分析文件的第一行，所以这个第一行实际就变成了key，之后的每一行内容变成了与之对应的value
    for row in reader:
        favorite = row["language"]
        #使用[""]表示row不再是每一行的具体内容，二是key+value的三个组合,循环表示依次把language这个key对应的value打印出来。
        print(favorite) #或者不需要声明变量favorite，直接print(row["language"])
        
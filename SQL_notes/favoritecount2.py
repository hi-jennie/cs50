import csv

from collections import Counter

with open("favorite.csv","r") as file:
    reader = csv.DictReader(file)
    counts = Counter #表示给了一个空白的dict
    
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1 #counter会自动初始化所有内容
            

for favorite, count in counts.most_common(): #使用most_common这个函数可以返回两个变量即key和value
    print(f"{favorite}:{count}")
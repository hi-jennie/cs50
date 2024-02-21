import csv

from collections import Counter

with open("favorite.csv","r") as file:
    reader = csv.DictReader(file)
    counts = {} #表示给了一个空白的dict
    
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1 #counter会自动初始化所有内容
            
favorite = input("favorite")

print(f"{favorite},{counts[favorite]}")
 #不全部打印出来，想看那个打印那个
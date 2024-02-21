#计数更简洁的方法1
import csv

with open("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    counts = {} #表示给了一个空白的dict
    
    for row in reader:
        favorite = row["genres"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

for favorite in counts:
    #for favorite in sorted(counts):  #如果改为这样则可以用python自带sorted函数对key按字母顺序排序
    #for favorite in sorted(counts，key=counts.get):get函数在此事dict counts自带的函数，即从counts中get value
    #for favorite in sorted(counts，key=counts.get,reverse=True):  可以按value反着排。
    print(f"{favorite}:{counts[favorite]}")  #?
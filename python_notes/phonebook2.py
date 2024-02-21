#使用key和value的方法查找（hash）
people = [
    {"name":"cater","number":"123456"} #这种方式其实有两个key，name和number
    {"name":"john","number":"654321"}
]

name = input("name:")

for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"found {number}") #这里的循环时按照上面的name和number的每一圈循环至结束
        #可以将前两行更改为  print(f"found {person['number']}")
else:
    print("not found")
    
    
    
    
#people = {
#    "carter":"123456",   #这个时候就只有名字本身是一个key，数字本身是一个value
#    "david":"654321",
}
#name = input ("name: ")
#
#if name in people:
#    number = people[name]
#    print(f"found{number}")
#else:
#    print("not found")
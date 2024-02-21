import csv

with open("favorite.csv","r") as file:
    reader = csv.DictReader(file)
    scrach, c, python = 0, 0, 0
    
    for row in reader:
        favorite = row["language"]
        if favorite == "scrach":
            scrach += 1
        elif favorite == "c":
            c += 1
        elif favorite == "python":
            python += 1
            
print(f"scrach:{scrach}")
print(f"c:{c}")
print(f"python:{python}")
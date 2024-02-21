from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite:")
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE provblem = ?",favorite)
#execute是sql自带的执行命令，即执行select后面的内容，favorite是传给“？”的参数。
row = rows[0]

print(row["n"]) #row代表rows中的第一行，此行命令表示打印这一行中n这个key对应的value。
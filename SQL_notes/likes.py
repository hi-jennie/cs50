#如何更新帖子的赞的数量
from cs50 import SQL
db =SQL("sqlite:///post")

db.execute("BEGIN,TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?",id);
likes = rows[0]["likes"]
db.execute("UPDATE posts SET likes = ? WHERE = ?",likes+1,id);
db.execute("commit")
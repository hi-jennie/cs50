#from cs50 import get_string
#answer = get_string("what's your name")
#print("hello, " + answer)  #python中与cl中不用%占位符将前后链接起来，直接用“+”
#print("hello,",answer) # 表示空格。2、3执行的结果一直，python会自动将二者连接起来
#print(f"hello,{answer}")  #在python中，在string前加入f则可以在该字符串内部使用{},print不会打印{}中的内容，而是打印插入花括号中的内容

answer = input("what's your name")
print(f"hello,{answer}") #和前一段执行效果一样，但是避免了get_string的冗长取而代之用input
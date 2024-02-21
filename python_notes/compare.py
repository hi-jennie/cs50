#1——python中conditionals的不同
#if x < y:
#   print("x is less than y")
#elif x > y:
#   print("x is greater than y")
#else
#    print("x is equal to y")


#2——
#from cs50 import get_int

#x = get_int("what's x")
#y = get_int("what's y")

#if x < y:
#   print("x is less than y")
#elif x > y:
#   print("x is greater than y")
#else:
#   print("x is equal to y")



#3——比较字符串
s = input("s: ")
t = input("t: ")

if s==t:
    print("same")
else:
    print("diferert")
#在c语言中，直接的s==t总会得出differert，因为c语言中的比较是比较的
#字符串的地址即char*所以无法直接比较，但是在python中可以直接比较。

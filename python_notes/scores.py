#scores = [72,73,33]
#使用方括号表示是个list
#averge = sum(scores) / len(scores)
##len表示上面list的长度即3
#print(f"Averge:{averge}")



#better
from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("score:")
    scores.append(score)
    #表示将用户那里获得的score加到scores列表中。也可以改为
    #scores = scores + [score]  
averge = sum(scores) / len(scores)
print(f"Averge:{averge}")
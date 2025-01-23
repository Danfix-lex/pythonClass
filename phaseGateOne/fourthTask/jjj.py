from random import randrange
answer = 0
for i in range(1, 100):
    for j in range(1, 100):
        answer = i + j
        if i + j == answer:
            print("correct")

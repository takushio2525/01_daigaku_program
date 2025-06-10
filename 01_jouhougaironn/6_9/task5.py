import random


def max_index(list):
    max = list[0]
    maxIndex=0
    for i in range(len(list)-1):
        if list[i+1] > max:
            max = list[i+1]
            maxIndex=i+1
    return maxIndex



def mymax(list):
    max = list[0]
    for i in range(len(list)-1):
        if list[i+1] > max:
            max = list[i+1]
    return max


n = 10
A = []

for i in range(n):
    A.append(random.randint(1, 100))

print("A=", A)

print("max=", mymax(A))
print("maxIndex=", max_index(A))

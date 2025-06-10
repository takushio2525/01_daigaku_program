import random
n = 10
A = []
for i in range(n):
    A.append(random.randint(1, 100))

print("A=", A)

max = A[0]
for i in range(len(A)-1):
    if A[i+1] > max:
        max = A[i+1]

print(max)

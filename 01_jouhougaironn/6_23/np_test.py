import numpy as np
a=np.array([1, 2, 3])
b=np.array([4, 5, 6])
n=len(a)

ip=0
for i in range(n):
    ip += a[i] * b[i]
print(ip)

pi=3.141592653589793
print(np.round(pi, 2))

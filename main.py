import random
import math
N = int(input("How many random points to generate? "))
n=0
i=0
while i < N:
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    if x**2 + y**2 < 1.0:
        n = n + 1

    i = i + 1
pi = 4.0*n/N
print(f"Pi is {pi}, error{math.pi - pi}")
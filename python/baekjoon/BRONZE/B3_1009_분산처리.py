import sys
import math
arr = []

n = int(input())

for i in range(n):
    [a, b] = sys.stdin.readline().rstrip().split(' ')
    a, b = int(a), int(b)
    arr.append([a, b])

for a, b in arr:
    loop = []
    for i in range(1, b+1):
        val = int(math.pow(a, i) % 10)
        if val not in loop:
            loop.append(val)
        else:
            break
    if loop[int(b%len(loop))-1] == 0:
        print(10)
    else:
        print(loop[int(b%len(loop))-1])
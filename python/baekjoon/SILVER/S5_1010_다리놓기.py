import math
import sys

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

num = int(input())
answer = []

for _ in range(num):
    r, n = sys.stdin.readline().rstrip().split(' ')
    r, n = int(r), int(n)
    answer.append(nCr(n,r))

for i in answer:
    print(i)


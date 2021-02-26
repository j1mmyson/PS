import sys

n, k = map(int, input().split())

d = {}
d2 = {}
for i in range(n):
    v = sys.stdin.readline().strip()
    d[v] = i+1
    d2[i+1] = v
for _ in range(k):
    v = sys.stdin.readline().strip()
    if v.isalpha():
        print(d[v])
    else:
        print(d2[int(v)])
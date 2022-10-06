import sys

n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
    x, y, z, r = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(r)

ab = {}
answer = 0

for x in a:
    for y in b:
        if ab.get(x+y):
            ab[x+y] += 1
        else:
            ab[x+y] = 1

for i in c:
    for j in d:
        v = (i + j) * (-1)
        if ab.get(v):
            answer += ab[v]

print(answer)


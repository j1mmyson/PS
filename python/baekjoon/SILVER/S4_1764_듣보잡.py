import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
answer = []

for _ in range(n):
    d[sys.stdin.readline().rstrip()] = True

for _ in range(m):
    v = sys.stdin.readline().rstrip()
    if d.get(v):
        answer.append(v)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
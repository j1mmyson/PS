import sys

l = []
n, _ = input().split()

visited = []
answer = 0

for i in range(int(n)+1):
    l.append([])

data = sys.stdin.read().splitlines()

for i in data:
    start, end = map(int, i.split())
    l[start].append(end)
    l[end].append(start)


for edge in range(1, int(n)+1):
    if edge in visited:
        continue
    answer += 1
    stack = [edge]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(l[v])
print(answer)
import sys

n = int(sys.stdin.readline())

edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    src, dst = map(int, sys.stdin.readline().split())
    edge[src].append(dst)
    edge[dst].append(src)

result = [0] * (n+1)

q = [1]
visited = [False] * (n+1)

while q:
    current = q.pop(0)
    if visited[current]:
        continue
    
    visited[current] = True

    for child in edge[current]:
        if not visited[child]:
            q.append(child)
            result[child] = current

for i in range(2, n+1):
    print(result[i])
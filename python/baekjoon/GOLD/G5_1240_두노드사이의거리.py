import sys

def getDistance(start, dst, node):
    distance = 0
    visited = [False] * len(node)

    q = [(start, 0)]
    
    while q:
        n, d = q.pop(0)
        if n == dst:
            distance = d
            break
        if not visited[n]:
            visited[n] = True
            for nn, dd in node[n]:
                q.append((nn, dd+d))
    return distance


n, m = map(int, sys.stdin.readline().split())

node = []
for _ in range(n+1):
    node.append([])

for _ in range(n-1):
    start, end, l = map(int, sys.stdin.readline().split())
    node[start].append((end, l))
    node[end].append((start, l))

for _ in range(m):
    start, dst = map(int, sys.stdin.readline().split())
    print(getDistance(start, dst, node))

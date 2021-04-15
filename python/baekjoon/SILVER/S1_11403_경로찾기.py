import sys
from collections import deque

def bfs(adj, start, target):
    visited = []
    q = deque([start])
    n = len(adj)

    while q:
        current = q.popleft()
        visited.append(current)
        if adj[current][target] == 1:
            return '1'
        for i in range(n):
            if adj[current][i] == 1 and i not in visited:
                q.append(i)
    return '0'
            

n = int(input())

adj = []
answer = []
for _ in range(n):
    adj.append(list(map(int, sys.stdin.readline().split(' '))))
    answer.append([])

for i in range(n):
    for j in range(n):
        answer[i].append(bfs(adj, i, j))

for i in answer:
    print(" ".join(i))



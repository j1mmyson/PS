import sys
from collections import deque

def dfs(tree, start):
    global n
    
    max_vertex, max_distance = 0, 0
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append([start, 0])

    while q:
        v, d = q.pop()
        visited[v] = True

        if d > max_distance:
            max_distance = d
            max_vertex = v
        
        for [next_vertex, next_distance] in tree[v]:
            if not visited[next_vertex]:
                q.append([next_vertex, d + next_distance])

    return [max_vertex, max_distance]


n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(1, n+1):
    inp = list(map(int, sys.stdin.readline().split()))
    start = inp[0]
    inp = inp[1:-1]

    for ind in range(0, len(inp), 2):
        destination, distance = inp[ind], inp[ind+1]
        tree[start].append([destination, distance])

edge, _ = dfs(tree, 1)
_, answer = dfs(tree, edge)
print(answer)

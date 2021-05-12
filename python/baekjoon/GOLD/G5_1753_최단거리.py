import sys
from collections import deque

v, n = map(int, sys.stdin.readline().split())
start = int(input())

edge = []
visited = []
answer = []
for _ in range(v+1):
    edge.append([])
    visited.append(False)
    answer.append(-1)
for _ in range(n):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append([v, w])


q = deque()

for i in edge[start]:
    q.append(i)
visited.append(start)
answer[start] = 0
while q:
    dst, w = q.popleft()
    if visited[dst] == False:
        visited[dst] = True
        answer[dst] = w
        for [v, weight] in edge[dst]:
            q.append([v, w+weight])

for i in answer[1:]:
    if i != -1:
        print(i)
    else:
        print("INF")

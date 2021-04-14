import sys
from collections import deque

def bfs(graph):
    answer = 0
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                answer += 1
                q = deque([(x, y)])
                currentColor = graph[x][y]
                while q:
                    i, j = q.popleft()
                    visited[i][j] = True
                    # left
                    if j != 0 and (i, j-1) not in q and visited[i][j-1] == False and graph[i][j-1] == currentColor :
                        q.append((i, j-1))
                    # right
                    if j != (n-1) and (i, j+1) not in q and visited[i][j+1] == False and graph[i][j+1] == currentColor:
                        q.append((i, j+1))
                    # up
                    if i != 0 and (i-1, j) not in q and visited[i-1][j] == False and graph[i-1][j] == currentColor:
                        q.append((i-1, j))
                    # down
                    if i != (n-1) and (i+1, j) not in q and visited[i+1][j] == False and graph[i+1][j] == currentColor:
                        q.append((i+1, j))
    return answer

num = int(input())
data = sys.stdin.read().splitlines()
graph = []
for i in data:
    temp = []
    for j in i:
        temp.append(j)
    graph.append(temp)

print(bfs(graph))
for i in range(num):
    for j in range(num):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
print(bfs(graph))
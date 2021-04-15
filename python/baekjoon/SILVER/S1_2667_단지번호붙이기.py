import sys
from collections import deque

def bfs(town):
    num = []
    n = len(town)
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visited[x][y] == False and town[x][y] == 1:
                count = 0
                q = deque([(x, y)])
                while q:
                    i, j = q.popleft()
                    visited[i][j] = True
                    # left
                    if j != 0 and (i, j-1) not in q and visited[i][j-1] == False and town[i][j-1] == 1 :
                        q.append((i, j-1))
                        count += 1
                    # right
                    if j != (n-1) and (i, j+1) not in q and visited[i][j+1] == False and town[i][j+1] == 1:
                        q.append((i, j+1))
                        count += 1
                    # up
                    if i != 0 and (i-1, j) not in q and visited[i-1][j] == False and town[i-1][j] == 1:
                        q.append((i-1, j))
                        count += 1
                    # down
                    if i != (n-1) and (i+1, j) not in q and visited[i+1][j] == False and town[i+1][j] == 1:
                        q.append((i+1, j))
                        count += 1
                
                num.append(count+1)
                
    return num

n = int(input())

town = []

for _ in range(n):
    line = sys.stdin.readline().strip()
    temp = []
    for i in line:
        temp.append(int(i))
    town.append(temp)

answer = bfs(town)

print(len(answer))
answer.sort()
for i in answer:
    print(i)

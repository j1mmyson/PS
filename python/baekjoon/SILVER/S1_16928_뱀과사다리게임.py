import sys
from collections import deque



def bfs(board):
    visited = []
    q = deque()
    q.append([1,0])
    while q:
        v, count = q.popleft()
        if v == 100:
            print(count)
            return
        if v in visited:
            continue
        visited.append(v)
        for i in range(1, 7):
            if v+i <= 100:
                q.append([board[v+i], count + 1])
    return

board = []
for i in range(101):
    board.append(i)

input()
data = sys.stdin.read().splitlines()

for line in data:
    i, j = map(int, line.split())
    board[i] = j


bfs(board)
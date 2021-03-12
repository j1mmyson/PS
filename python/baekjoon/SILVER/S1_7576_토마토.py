import sys
from collections import deque

def isFinish(m):
    for i in m:
        for j in i:
            if j == 0:
                return False
    return True

c, r = map(int, input().split())

data = sys.stdin.read().splitlines()
box = []

for i in data:
    box.append(list(map(int, i.split())))

stack = deque()
for i in range(r):
    for j in range(c):
        if box[i][j] != 0 and box[i][j] != -1:
            stack.append([i, j, 1])
maxDept = 0
while stack:
    [i, j, d] = stack.popleft()
    if d > maxDept:
        maxDept = d
    d += 1
    if j != 0 and box[i][j-1] == 0:
        stack.append([i, j-1, d])
        box[i][j-1] = d
    # right
    if j != (c-1) and box[i][j+1] == 0:
        stack.append([i, j+1, d])
        box[i][j+1] = d
    # up
    if i != 0 and box[i-1][j] == 0:
        stack.append([i-1, j, d])
        box[i-1][j] = d
    # down
    if i != (r-1) and box[i+1][j] == 0:
        stack.append([i+1, j, d])
        box[i+1][j] = d

if isFinish(box):
    print(maxDept-1)
else:
    print(-1)

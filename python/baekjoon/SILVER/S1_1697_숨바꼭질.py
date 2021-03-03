import sys
from collections import deque

def move(locate, target):
    count = 0
    q = deque([[locate, count]])

    while q:
        [loc, count] = q.popleft()
        if visited[loc]:
            continue
        visited[loc] = True
        if loc == target:
            return count
        if loc -1 >= 0:
            q.append([loc-1, count+1])
        if loc+1 <= 100000:
            q.append([loc+1, count+1])
        if loc*2 <= 100000:
            q.append([2*loc, count+1])
    
    return -1
        

n, k = map(int, sys.stdin.readline().split())
# global visited
visited = [False] * 100001
print(move(n, k))
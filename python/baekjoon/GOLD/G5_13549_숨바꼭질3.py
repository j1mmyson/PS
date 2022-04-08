import sys
from collections import deque

src, dst = map(int, sys.stdin.readline().split())
MAX = 100001

dp = [0] * MAX
dp[src] = 0
visited = [False] * MAX

q = deque()
q.append(src)

while q:
    current = q.popleft()
    if current == dst:
        break
    if current * 2 < MAX:
        if not visited[current * 2]:
            dp[current * 2] = dp[current]
            visited[current * 2] = True
            q.appendleft(current * 2)
    if current + 1 < MAX:
        if not visited[current + 1]:
            dp[current + 1] = dp[current] + 1
            visited[current + 1] = True
            q.append(current + 1)
    if current - 1 >= 0:
        if not visited[current - 1]:
            dp[current - 1] = dp[current] + 1
            visited[current - 1] = True
            q.append(current - 1)

print(dp[dst])

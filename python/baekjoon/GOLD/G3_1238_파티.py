import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
INF = int(1e9)
path = [[] for _ in range(n+1)]
res = [0] * (n+1)
rx = []

for _ in range(m):
    s, e, d = map(int, sys.stdin.readline().split())
    path[s].append((e, d))

for i in range(1, n+1):

    distance = [INF] * (n+1)
    distance[i] = 0
    q = [[distance[i], i]]

    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_distance > distance[current_node]:
            continue

        for nn, dd in path[current_node]:
            if distance[nn] > current_distance + dd:
                distance[nn] = current_distance + dd
                heapq.heappush(q, [distance[nn], nn])

    if i == x:
        rx = distance
    else:
        res[i] = distance[x]

res = [x+y for x, y in zip(res, rx)]
print(max(res[1:]))

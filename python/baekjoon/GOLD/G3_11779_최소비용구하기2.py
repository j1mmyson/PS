import sys
import heapq

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

path = [[] for _ in range(n)]
for _ in range(p):
    s, e, v = map(int, sys.stdin.readline().split())
    path[s-1].append([e-1, v])

start, end = map(int, sys.stdin.readline().split())

vst = []
distance = [[2**31, []] for _ in range(n)]
distance[start-1][0] = 0

q = [[0, start-1, []]]

while q:
    v, node, rec = heapq.heappop(q)
    if distance[node][0] < v:
        continue
    
    for nn, nv in path[node]:
        d = v + nv
        if d < distance[nn][0]:
            distance[nn][0] = d
            distance[nn][1] = rec + [node]
            heapq.heappush(q, [d, nn, rec + [node]])

print(distance[end-1][0])
print(len(distance[end-1][1])+1)
for i in distance[end-1][1]:
    print(i+1, end=' ')

print(end)

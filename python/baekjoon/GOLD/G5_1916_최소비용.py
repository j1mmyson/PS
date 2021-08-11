import heapq
import sys

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]


for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus[start].append([end, cost])
    
src, dst = map(int, sys.stdin.readline().split())

distance = [sys.maxsize] * (n+1)
distance[src] = 0

q = []
heapq.heappush(q, (0, src))

while q:
    current_distance, current_destination = heapq.heappop(q)

    if distance[current_destination] < current_distance:
        continue

    for new_destination, new_distance in bus[current_destination]:
        d = current_distance + new_distance
        if d < distance[new_destination]:
            distance[new_destination] = d
            heapq.heappush(q, (d, new_destination))

print(distance[dst])
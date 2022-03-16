import sys
import heapq

n = int(input())

heap = []

for _ in range(n):
    inp = int(sys.stdin.readline())
    if inp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [abs(inp), inp])

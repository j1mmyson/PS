import sys
import heapq

input()

data = sys.stdin.read().splitlines()
heap = []

for item in data:
    value = int(item)
    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-value, value))

import heapq
import sys

n = int(input())
q = []

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == '0':
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, int(cmd))
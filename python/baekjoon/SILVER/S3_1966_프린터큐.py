import sys
import heapq

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    maxq = []
    for i in l:
        heapq.heappush(maxq, -i)
    res = 0
    ind = m

    currentMax = -heapq.heappop(maxq)
    while True:
        if l[0] == currentMax:  # pop을 할 때
            res += 1
            if ind == 0:
                break
            currentMax = -heapq.heappop(maxq)
            n -= 1
            l.pop(0)
        else:   # pop을 하지 않을 때
            l.append(l.pop(0))

        if ind == 0:
            ind = n-1
        else:
            ind -= 1
        # l.append(l.pop(0))
    print(res)

import sys
import heapq

m, n = map(int, sys.stdin.readline().split())
tp = [0]
appears = []

answer = 0
maxTemp = 0
ind = 0

money = [0] * 15000

for _ in range(m):
    tp.append(int(input()))

for _ in range(n):
    s, e, t = map(int, sys.stdin.readline().split())
    price = (e-s) * tp[t]
    heapq.heappush(appears, [e, s, price])

while appears:
    e, s, price = heapq.heappop(appears)
    for i in range(ind, e+1):
        if i == e:
            money[i] = max(maxTemp, money[s] + price)
            maxTemp = max(maxTemp, money[s] + price)
        else:
            money[i] = maxTemp
    ind = e

print(maxTemp)

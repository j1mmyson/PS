import sys

n, k = map(int, sys.stdin.readline().split())

coin = []
count = 0
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

while coin:
    m = coin.pop()
    if k >= m:
        n = k // m
        k = k - n*m
        count += n
    if k == 0:
        break

print(count)
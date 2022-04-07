import sys
import copy

n = int(sys.stdin.readline())

temp = list(map(int, sys.stdin.readline().split()))
maxdp = temp
mindp = temp

for _ in range(n-1):
    x, y, z = map(int, sys.stdin.readline().split())
    maxdp = [max(maxdp[0], maxdp[1]) + x, max(maxdp) + y, max(maxdp[1], maxdp[2]) + z]
    mindp = [min(mindp[0], mindp[1]) + x, min(mindp) + y, min(mindp[1], mindp[2]) + z]

print(max(maxdp))
print(min(mindp))
    
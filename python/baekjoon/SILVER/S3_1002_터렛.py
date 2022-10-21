import sys;
import math
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    r = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if r1+r2 == r or abs(r1-r2) == r:
        print(1)
    elif r1+r2 > r and r > abs(r2-r1):
        print(2)
    else:
        print(0)

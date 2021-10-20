import sys

[x1, y1] = map(int, sys.stdin.readline().split())
[x2, y2] = map(int, sys.stdin.readline().split())
[x3, y3] = map(int, sys.stdin.readline().split())

l = (x2-x1) * (y3-y1)
r = (y2-y1) * (x3-x1)

if l > r:
    print(1)
elif l < r:
    print(-1)
else:
    print(0)

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    l = sorted([a, b, c])

    if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        print("right")
    else:
        print("wrong")


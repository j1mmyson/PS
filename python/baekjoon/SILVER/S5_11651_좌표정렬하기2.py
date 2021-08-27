import sys

n = int(input())

cor = []

for _ in range(n):
    [x, y] = map(int, sys.stdin.readline().split())
    cor.append([x, y])

cor = sorted(cor, key=lambda x : (x[1], x[0]))

for i in cor:
    print(i[0], i[1])
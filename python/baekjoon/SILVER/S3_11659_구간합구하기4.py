import sys

n, m = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
sumList = [0]
s = 0
for n in num:
    s += n
    sumList.append(s)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sumList[j] - sumList[i-1])

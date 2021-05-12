import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
l = []
for _ in range(n):
    l.append(0)
l[0] = 1

for i in range(1, n):
    correntValue = arr[i]
    cand = []
    for j in range(i):
        if correntValue > arr[j]:
            cand.append(l[j])
    if cand == []:
        l[i] = 1
    else:
        l[i] = max(cand) + 1

print(max(l))

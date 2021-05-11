import sys

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for a in range(1, len(arr)):
    for i in range(3):
        if i == 0:
            arr[a][i] += min(arr[a-1][1:])
            
        elif i == 1:
            arr[a][i] += min(arr[a-1][0], arr[a-1][2])
        else:
            arr[a][i] += min(arr[a-1][:2])


print(min(arr[-1]))


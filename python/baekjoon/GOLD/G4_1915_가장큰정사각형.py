import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
answer = 0

for _ in range(n):
    inp = sys.stdin.readline().rstrip()
    arr.append(list(map(int, list(inp))))

for i in range(n):
    if arr[i][0] == 1:
        answer = 1
for j in range(m):
    if arr[0][j] == 1:
        answer = 1


for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            temp = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])
            if temp == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = temp + 1
                answer = max(answer, arr[i][j])

print(answer**2)

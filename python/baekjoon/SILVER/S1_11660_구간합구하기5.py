import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
dp = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    dp.append([0] * n)

dp[0][0] = arr[0][0]
for i in range(n):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i][j] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        temp = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        print(temp)



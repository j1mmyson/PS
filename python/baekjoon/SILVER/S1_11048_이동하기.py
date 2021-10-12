import sys

n, m = map(int, sys.stdin.readline().split())

miro = []
dp = []

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().split())))
    dp.append([0]*m)

dp[0][0] = miro[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + miro[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + miro[0][j]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + miro[i][j]

print(dp[-1][-1])
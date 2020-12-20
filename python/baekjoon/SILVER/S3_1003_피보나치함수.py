import sys

n = int(sys.stdin.readline().rstrip())
arr = list()


for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [[1, 0], [0, 1]]

for i in range(2, 40):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])

for n in arr:
    print(dp[n][0], dp[n][1])
import sys

n = int(input())
dp = [1, 1, 1, 2, 2]
l = []

for _ in range(n):
    l.append(int(input()))


for i in range(5, max(l)):
    dp.append(dp[i-1] + dp[i-5])

for i in l:
    print(dp[i-1])
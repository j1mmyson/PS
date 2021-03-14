import sys

input()

data = sys.stdin.read().splitlines()
dp = [1, 2, 4]

for i in range(3,11):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for i in data:
    print(dp[int(i)-1])
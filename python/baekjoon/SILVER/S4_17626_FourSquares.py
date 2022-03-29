import sys
import math
n = int(sys.stdin.readline())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n+1):
    temp = 1e9
    j = 1
    for j in range(1, int(math.sqrt(i)) + 1):
        temp = min(temp, dp[i - j ** 2])
    dp[i] = temp + 1
print(dp[n])

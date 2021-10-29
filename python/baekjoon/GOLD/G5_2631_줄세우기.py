import sys

input = sys.stdin.readline
n = int(input())

arr = []
dp = []
maxValue = 0
for _ in range(n):
    arr.append(int(input()))
    dp.append(0)


for i in range(n):
    dp[i] = 1
    for j in range(0, i):
        if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
    
    if dp[i] > maxValue:
        maxValue = dp[i]
print(n-maxValue)
import sys
input = sys.stdin.readline

def getNum(target, coin):
    dp = [0] * (target+1)
    dp[0] = 1
    for c in coin:
        for i in range(1, target+1):
            if i - c >= 0:
                dp[i] = dp[i-c] + dp[i]
    
    return dp[-1]

n = int(input())

for _ in range(n):
    cn = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    print(getNum(target, coin))
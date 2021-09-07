from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == math.inf:
            return -1
        return dp[amount]

testCase = {
        'coins': [1, 2, 5],
        'amount': 11,
        'expected': 3
}

s = Solution()
result = s.coinChange(testCase['coins'], testCase['amount'])
if result == testCase['expected']:
        print("Success!")
        print("result = ", result, "\nexpected = ", testCase['expected'])
else:
        print("Failed;")
        print("result = ", result, "\nexpected = ", testCase['expected'])

class Solution:
    def reverse(self, x: int) -> int:
        maxValue = 2**31 -1
        isNegative = False
        if x < 0:
            isNegative = True
            x = x * (-1)
        stringX = str(x)[::-1]
        x = int(stringX)
        if (x >= maxValue) or (x <= (-1)*maxValue):
            return 0
        if isNegative:
            return x * (-1)
        return x

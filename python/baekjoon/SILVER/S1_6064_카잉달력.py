import sys

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x


def lcm(x, y):
    result = (x*y)//gcd(x, y)
    return result


n = int(input())

for _ in range(n):
    M, N, x, y = map(int, sys.stdin.readline().split())
    num = -1
    xList = []
    yList = []
    maxNum = lcm(M, N)
    while x <= maxNum:
        if (x - y) % N == 0:
            num = x
            break
        x += M
    if num == -1:
        print(-1)
    else:
        print(num)


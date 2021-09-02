import sys, math

def getChild(n, m):
    v = 1
    for i in range(m):
        v *= n
        n -= 1

    return v

n, m = map(int, sys.stdin.readline().split())
if n < 2*m:
    m = n-m

print(getChild(n, m) // math.factorial(m))

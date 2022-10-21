import sys
import math

def isPrime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True


m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)

import sys

def getFibo(n):
    if not fibo.get(n):
        if n % 2 == 1:
            fibo[n] = (getFibo((n+1)//2)**2 + getFibo((n+1)//2-1)**2) % 1000000007
        else:
            fibo[n] = (getFibo(n+1) - getFibo(n-1)) % 1000000007

    return fibo[n]


n = int(sys.stdin.readline())
fibo = {0: 0, 1: 1, 2: 1}

print(getFibo(n))
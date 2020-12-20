import sys

def gcd(a, b): # 최대공약수
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

[n, n2] = sys.stdin.readline().rstrip().split(' ')


n, n2 = int(n), int(n2)

gcd = gcd(n, n2)

ans = ''
for i in range(gcd):
    ans += '1'

print(ans)
import sys

def solve(a, b, c):
    if b == 1:
        return a % c
    if b%2 == 0:
        b = solve(a, b//2, c)
        return (b * b) % c
    else:
        b = solve(a, b//2, c)
        return (b * b * a) % c

    
    

a, b, c = map(int, sys.stdin.readline().split())
print(solve(a,b,c))
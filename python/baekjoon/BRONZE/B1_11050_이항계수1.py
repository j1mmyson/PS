import sys

def nk(n, k):
    if k == 0 or k == n:
        return 1
    
    return nk(n-1, k-1) + nk(n-1, k)

n, k = map(int, sys.stdin.readline().split())

print(nk(n, k))
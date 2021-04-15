import sys

def isFilled(m):
    for i in m:
        for j in i:
            if j == 0:
                return False
    
    return True

def slicing(m, r, c):
    s = m[r[0]:r[1]]
    result = []
    for i in s:
        result.append(s[c[0]:c[1]])
    return result

def sol(m, n):
    if isFilled(m):
        return 1
    return sol(m[0:n//2]) + sol() + sol() + sol()

 
n = int(input())
data = sys.stdin.read().splitlines()
m = []
for i in data:
    row = list(map(int, i.split()))
    m.append(row)


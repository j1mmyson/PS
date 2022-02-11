import sys

def dfs(start:int):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n):
        s.append(l[i])
        dfs(i)
        s.pop()


n, m = map(int, sys.stdin.readline().split())
l = sorted(list(map(int, sys.stdin.readline().split())))
s = []
dfs(0)

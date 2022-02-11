import sys

def dfs(start:int):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if len(s) == 0:
            s.append(i)
            dfs(i+1)
            s.pop()
        elif (len(s) != 0) and (i >= s[-1]):
            s.append(i)
            dfs(i+1)
            s.pop()


n, m = map(int, sys.stdin.readline().split())
s = []

dfs(1)

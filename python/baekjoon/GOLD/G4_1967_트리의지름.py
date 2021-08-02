import sys

def bfs(v, n):
    visited = [0] * (n+1)
    w = 0
    q = [(v, w)]
    l = []
    
    while(q):
        v, w = q.pop(0)
        if visited[v]:
            continue
        
        visited[v] = 1
        l.append((w, v))
        if not d.get(v):
            continue
        
        for i in range(len(d[v])):
            q.append([d[v][i][0], w + d[v][i][1]])
    
    ml, mv = max(l)[0], max(l)[1]
    return [ml, mv]


d = {}

num = int(input())
answer = []

for _ in range(num-1):
    root, dst, weight = map(int, sys.stdin.readline().split())
    if not d.get(root):
        d[root] = [[dst, weight]]
    else:
        d[root].append([dst, weight])

    if not d.get(dst):
        d[dst] = [[root, weight]]
    else:
        d[dst].append([root, weight])

if num == 1:
    print(0)
elif num == 2:
    print(d[1][0][1])
else:
    v = bfs(1, num)[1]
    answer = bfs(v, num)[0]
    print(answer)
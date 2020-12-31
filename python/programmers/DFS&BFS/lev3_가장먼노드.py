def bfs(v, l, visited):
    global d
    depth = 0
    q = [(v, depth)]
    
    while(q):
        v, depth = q.pop(0)
        if not visited[v]:
            d[v] = depth
            visited[v] = True
            depth += 1
            for i in l[v]:
                q.append([i, depth])

def solution(n, edge):
    answer = 0
    global d
    d = [0] * (n+1)
    d[1] = 1
    l = list()
    visited = [False] * (n+1)
    
    for i in range(n+1):
        l.append([])
    
    for (i, j) in edge:
        if j not in l[i]:
            l[i].append(j)
        if i not in l[j]:
            l[j].append(i)
    
    bfs(1, l, visited)
    
    for i in d:
        if i == max(d):
            answer += 1
    return answer
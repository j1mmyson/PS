from collections import deque

def s(adj):
    global q
    global zz
    global result
    que = deque()
    que.append([0, 0, 0, False])
    
    while que:
        [n, coin, time, tel] = que.popleft()
        if coin in q:
            if result[q.index(coin)] == -1:
                result[q.index(coin)] = time
        if coin > q[-1]:
            continue
        que.append([n, coin+zz, time+1, False])
        for i in range(len(adj)):
            if i != n and tel == False:
                que.append([i, coin, time+1, True])
            if adj[n][i] != 0:
                que.append([i, coin+adj[n][i], time+1, False])

        
        

def bfs(n, coin, adj, time, tel):
    global q
    global zz
    if coin in q:
        if result[q.index(coin)] == -1:
            result[q.index(coin)] = time
    if coin > q[-1]:
        return
    # 아무것도 안하고 z원 
    bfs(n, coin+zz, adj, time + 1, False)
    # 다른 도시로 이동
    for i in range(len(adj)):
        if i != n and tel == False:
            bfs(i, coin, adj, time+1, True)
        if adj[n][i] != 0:
            bfs(i, coin + adj[n][i], adj, time+1, False)
    # 다른 도시로 순간이동
    
    

def solution(n, z, roads, queries):
    answer = [-1] * len(queries)
    global result
    result = answer
    global q
    global zz
    zz = z
    q = sorted(queries)
    m = []
    for _ in range(n):
        m.append([0]*n)
    
    for [i, j, w] in roads:
        m[i][j] = w
    # bfs(0, 0, m, 0, False)
    s(m)
    
    
    return result
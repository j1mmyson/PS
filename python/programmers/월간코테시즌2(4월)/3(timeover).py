from collections import deque

def travel(adj, w, start, m):
    s = 0
    visited = [False for _ in range(len(w))]
    visited[start] = True
    q = deque([[start, 0]])
    
    while q:
        v, d = q.popleft()
        s += d * abs(w[v])
        if s >= m:
            return s
        for i in adj[v]:
            if not visited[i]:
                visited[i] = True
                q.append([i, d+1])
    return s

def solution(a, edges):
    if sum(a) != 0:
        return -1
    adj = []
    for _ in range(len(a)):
        adj.append([])
    
    for [i, j] in edges:
        adj[i].append(j)
        adj[j].append(i)
    
    m = 1000000
    answer = []
    for i in range(1, len(a)):
        answer.append(travel(adj, a, i, m))
        # m = min(m, travel(adj, a, i, m))
    
    return min(answer)
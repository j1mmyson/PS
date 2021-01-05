import sys

def DFS(graph, start):
    for i in graph:
        i.sort(reverse=True)
    result = []
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            result.append(node)
            stack.extend(graph[node])
    return result

def BFS(graph, start):
    for i in graph:
        i.sort()
    result = []
    visited = []
    q = [start]

    while q:
        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            result.append(node)
            q.extend(graph[node])
    return result


V, M, start = sys.stdin.readline().rstrip().split(' ')
V, M, start = int(V), int(M), int(start)

graph = []
visited = []
for _ in range(V+1):
    graph.append([])

for _ in range(M):
    [i, j] = sys.stdin.readline().rstrip().split(' ')
    i, j = int(i), int(j)
    graph[i].append(j)
    graph[j].append(i)

dfs = DFS(graph, start)
bfs = BFS(graph, start)

for i in dfs:
    print(i, end=' ')

print()
for i in bfs:
    print(i, end=' ')

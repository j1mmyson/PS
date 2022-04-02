import sys

n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

graph = list()
for i in range(n):
    graph.append([])


road = []
se = []
for _ in range(n - 1):
    road.append(list(map(int, sys.stdin.readline().split())))

for i in range(q):
    se.append(list(map(int, sys.stdin.readline().split())))

for [s, e] in road:
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

def dfs(graph, start, end):
    visited = []
    rec = []
    stack = [[start, rec]]
    while stack:
        node, rec = stack.pop()
        if node == end:
            return rec + [end]
        if node not in visited:
            visited.append(node)
            rec.extend([node])
            for i in graph[node]:
                stack.append([i, rec])
    return []

for [s, e] in se:
    if s == e:
        print(a[s-1])
    else:
        answer = ""
        path = dfs(graph, s-1, e-1)
        for i in path:
            answer += str(a[i])
            answer = str(int(answer) % 1000000007)
        print(answer)

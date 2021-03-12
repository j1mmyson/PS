import sys

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return len(visited)

n = int(input())
input()
data = sys.stdin.read().splitlines()

graph = []

for i in range(n+1):
    graph.append([])

for i in data:
    [v, dst] = map(int, i.split())
    graph[v].append(dst)
    graph[dst].append(v)

answer = dfs(graph, 1) - 1
print(answer)


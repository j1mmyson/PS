import sys

def getKevin(relation, start):
    kevin = 0
    que = [[start,0]]
    visited = []

    while que:
        v, dpt = que.pop(0)
        if v in visited:
            continue
        kevin += dpt
        visited.append(v)
        for i in relation[v]:
            que.append([i, dpt+1])
    return kevin


n, m = map(int, input().split())

r = []
answer = []
for _ in range(n+1):
    r.append([])
relation = sys.stdin.read().splitlines()

for row in relation:
    i, j = map(int, row.split())
    r[i].append(j)
    r[j].append(i)

for i in range(1, n+1):
    answer.append(getKevin(r, i))

print(answer.index(min(answer))+1)

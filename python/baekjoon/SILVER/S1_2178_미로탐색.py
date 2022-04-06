import sys

n, m = map(int, sys.stdin.readline().split())

miro = []
distance = [[2 ** 31 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().strip())))

q = [(0, 0, 1, [])]

while q:
    x, y, d, vst = q.pop(0)
    
    if x < 0 or x >= n or y < 0 or y >= m:
        continue
    
    if (x, y) in vst:
        continue

    next = miro[x][y]
    if next == 1:
        vst.append((x, y))
        if d < distance[x][y]:
            distance[x][y] = d
        q.append((x-1, y, d+1, vst))
        q.append((x, y-1, d+1, vst))
        q.append((x+1, y, d+1, vst))
        q.append((x, y+1, d+1, vst))

print(distance[-1][-1])

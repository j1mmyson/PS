import sys
from itertools import combinations

def getDistance(home, chicken):
    distance = 0
    for h in home:
        d = []
        x, y = h[0], h[1]
        for c in chicken:
            d.append(abs(c[0] - x) + abs(c[1] - y))
        distance += min(d)
    return distance

n, m = map(int, sys.stdin.readline().split())

town = []
for _ in range(n):
    town.append(list(map(int, sys.stdin.readline().split())))

chicken = []
home = []
distance = []
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            home.append([i, j])
        elif town[i][j] == 2:
            chicken.append([i, j])

chickenComb = combinations(chicken, m)

for comb in chickenComb:
    d = getDistance(home, comb)
    if d < answer:
        answer = d

print(answer)
import sys

n, k = map(int, sys.stdin.readline().split())

bag = {0: 0}

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    temp = {}
    for key, value in bag.items():
        if key + w <= k and v + value > bag.get(key + w, 0):
            temp[key + w] = v + value
    bag.update(temp)

print(max(bag.values()))
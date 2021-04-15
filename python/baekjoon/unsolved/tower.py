import sys

n = sys.stdin.readline().rstrip()
tower = sys.stdin.readline().rstrip().split()
tower = list(map(int, tower))

max = 0

for i, hi in enumerate(tower):
    for j, hj in enumerate(tower[i:]):
        val = j*(hi + hj)
        if max < val:
            max = val

print(max)
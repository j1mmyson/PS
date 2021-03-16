import sys, copy
input()

data = list(map(int, sys.stdin.readline().split()))
cp = copy.deepcopy(data)

cp.sort()
d = {}
count = 0
for i in cp:
    if i not in d:
        d[i] = count
        count += 1

for i in data:
    print(d[i], end=" ") 
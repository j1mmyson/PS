import sys

input()
data = sys.stdin.read().splitlines()
l = []
answer = 0

for line in data:
    l.append(list(map(int, line.split())))

l = sorted(l, key=lambda l: (l[1], l[0]))
time = 0

for i in l:
    if time > i[0]:
        continue
    answer += 1
    time = i[1]

print(answer)
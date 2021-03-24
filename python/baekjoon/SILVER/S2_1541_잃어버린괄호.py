import sys

data = sys.stdin.readline().strip()

data = data.split('-')
s = 0
for i in range(1, len(data)):
    data[i] = list(map(int, data[i].split('+')))
    data[i] = sum(data[i])
    s = s + data[i]

data[0] = list(map(int, data[0].split('+')))
data[0] = sum(data[0])

print(data[0] - s)
import sys

i, j = map(int, sys.stdin.readline().split())
m = []
for _ in range(i):
    row = list(sys.stdin.readline().rstrip())
    m.append(row)
answer = 0

for x in range(i):
    for y in range(j):
        if m[x][y] == '-':
            if y == 0:
                answer += 1
            else:
                if m[x][y-1] == '-':
                    continue
                else:
                    answer += 1
        else:
            if x == 0:
                answer += 1
            else:
                if m[x-1][y] == '|':
                    continue
                else:
                    answer += 1

print(answer)
                
import sys

input()

data = list(map(int, sys.stdin.read().splitlines()))

answer = []
for i in range(len(data)):
    answer.append([0, 0])

answer[0] = [data[0], data[0]]
if len(data) == 1:
    pass
else:
    answer[1] = [data[0]+data[1], data[1]]
    for i in range(2, len(answer)):
        answer[i][0] = answer[i-1][1] + data[i]
        answer[i][1] = max(answer[i-2]) + data[i]

print(max(answer[-1]))
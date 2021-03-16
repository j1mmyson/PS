import sys

input()
l = list(map(int, sys.stdin.readline().split()))
l.sort()
answer = [l[0]]

for i in range(1, len(l)):
    answer.append(answer[i-1] + l[i])

print(sum(answer))
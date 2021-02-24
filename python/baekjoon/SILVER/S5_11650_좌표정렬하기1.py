import sys
input()

answer = []
data = sys.stdin.read().splitlines()
for line in data:
    x, y = map(int, line.split())
    answer.append((x, y))

answer = sorted(answer, key=lambda x : (x[0], x[1]))
for locate in answer:
    print(locate[0], locate[1])

n, k = map(int, input().split())

q = []
answer = []

for i in range(1, n+1):
    q.append(i)

while(True):
    if len(q) == 0:
        break
    for i in range(k-1):
        q.append(q.pop(0))
    answer.append(str(q.pop(0)))

print("<", end='')
print(', '.join(answer), end ='')
print(">")
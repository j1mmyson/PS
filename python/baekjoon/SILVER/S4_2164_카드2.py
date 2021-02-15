from collections import deque

n = int(input())
arr = deque()
for i in range(1, n+1):
    arr.append(i)

while(True):
    if len(arr) == 1:
        break
    arr.popleft()
    arr.append(arr.popleft())

print(arr.popleft())
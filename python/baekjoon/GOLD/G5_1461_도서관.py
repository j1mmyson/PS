import sys

n, m = map(int, sys.stdin.readline().split())

books = list(map(int, sys.stdin.readline().split()))

left = []
right = []
for book in books:
    if book < 0:
        left.append(abs(book))
    else:
        right.append(abs(book))
    
left.sort()
right.sort()

walks = 0
answer = 0

if not left:
    maxValue = right[-1]
    if len(right) <= m:
        right = []
    else:
        right = right[:-m]
elif not right:
    maxValue = left[-1]
    if len(left) <= m:
        left = []
    else:
        left = left[:-m]
elif left[-1] >= right[-1]:
    maxValue = left[-1]
    if len(left) <= m:
        left = []
    else:
        left = left[:-m]
else:
    maxValue = right[-1]
    if len(right) <= m:
        right = []
    else:
        right = right[:-m]

while True:
    if len(left) == 0:
        break
    if len(left) <= m:
        answer += 2 * left[-1]
        break
    answer += 2 * left[-1]
    left = left[:-m]

while True:
    if len(right) == 0:
        break
    if len(right) <= m:
        answer += 2 * right[-1]
        break
    answer += 2 * right[-1]
    right = right[:-m]

answer += maxValue
print(answer)



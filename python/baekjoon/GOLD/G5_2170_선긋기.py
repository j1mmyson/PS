import sys

n = int(input())
lines = []

for i in range(n):
    [l, r] = sys.stdin.readline().rstrip().split(' ')
    l, r = int(l), int(r)
    if l > r:
        temp = l
        l = r
        r = temp
    lines.append([l, r])

lines.sort()

l = lines[0][0]
r = lines[0][1]
lensum = 0

for left, right in lines:
    if r < left:
        lensum += r-l
        l = left
        r = right
    else:
        r = max(r, right)

lensum += r - l

print(lensum)
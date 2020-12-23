n = int(input())

answer = 0

zero, left, right = 1, 1, 1

for i in range(1, n):
    zero, left, right = (zero+left+right)%9901, (zero+right)%9901, (zero+left)%9901

answer = (zero+left+right)%9901
print(answer)
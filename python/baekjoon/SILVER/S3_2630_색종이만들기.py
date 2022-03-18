import sys

square = []
paper = [0, 0]
n = int(sys.stdin.readline())

for _ in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))

def solution(x, y, n):
    color = square[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != square[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        paper[0] += 1
    else:
        paper[1] += 1

solution(0, 0, n)
print(paper[0])
print(paper[1])

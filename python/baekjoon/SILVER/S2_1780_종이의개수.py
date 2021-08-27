import sys

def devide(paper):
    l = len(paper)//3

    for i in range(3):
        for j in range(3):
            rowStart = l*i
            colStart = l*j
            check([row[colStart:colStart+l] for row in paper[rowStart:rowStart+l]])
    return


def check(x, y, n):
    p = paper[x][y]
    global res

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != p:
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3, y+l*n//3, n//3)
                return
    res[p] += 1
    return


n = int(input())
paper = []
res = {}
res[-1] = 0
res[0] = 0
res[1] = 0
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

check(0, 0, n)

print(res[-1])
print(res[0])
print(res[1])

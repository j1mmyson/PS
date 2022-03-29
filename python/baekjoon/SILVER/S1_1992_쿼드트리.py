import sys

n = int(sys.stdin.readline())
m = []

for _ in range(n):
    m.append(list(map(int, sys.stdin.readline().strip())))

def zip(x, y, n):
    canZip = m[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if m[i][j] != canZip:
                canZip = -1
                break

    if canZip == -1:
        n = n // 2
        print("(", end = '')
        zip(x, y, n)
        zip(x, y + n, n)
        zip(x + n, y, n)
        zip(x + n, y + n, n)
        print(")", end = '')
    elif canZip == 1:
        print(1, end = '')
    else:
        print(0, end = '')

zip(0, 0, n)

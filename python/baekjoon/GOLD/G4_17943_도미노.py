import sys

n, q = map(int, sys.stdin.readline().split())

dn = list(map(int, sys.stdin.readline().split()))

domino = [0]

for d in dn:
    last = domino[-1]
    domino.append(last ^ d)

for _ in range(q):
    question = list(map(int, sys.stdin.readline().split()))
    if question[0] == 0:
        [x, y] = question[1:]
        print(domino[x-1] ^ domino[y-1])
    else:
        [x, y, d] = question[1:]
        temp = domino[x-1] ^ domino[y-1]
        print(d ^ temp)



import sys

def LIS(l:list) -> list:
    length = []
    for i in range(len(l)):
        length.append(1)
        for j in range(0, i):
            if (l[j] < l[i]):
                length[i] = max(length[i], length[j] + 1)
    return length


def LDS(l:list) -> list:
    length = []
    for i in range(len(l)):
        length.append(1)
        for j in range(0, i):
            if (l[j] > l[i]):
                length[i] = max(length[i], length[j] + 1)
    return length


n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

answer = 0
lis = LIS(l)
lds = LIS(l[::-1])[::-1]

for i in range(n):
    answer = max(answer, lis[i] + lds[i])

print(answer-1)

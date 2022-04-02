import sys

n = int(sys.stdin.readline())
potion = list(map(int, sys.stdin.readline().split()))
sale = [[] for _ in range(n)]
visited = [False] * n
result = 0

for i in range(n):
    tn = int(sys.stdin.readline())
    for _ in range(tn):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        sale[i].append([x, y])


for _ in range(n):  # 4번 구매
    minimum = [0, 2**31 - 1]
    for i in range(n): # 전체 순회
        if not visited[i]:
            if potion[i] == 1:
                minimum = [i, 0]
                break
            temp = potion[i]
            for [j, k] in sale[i]:
                if not visited[j]:
                    t = potion[j] - k
                    if t < 1:
                        t = potion[j] - 1
                    else:
                        t = k
                    temp -= t
            if temp < minimum[1]:
                minimum = [i, temp]
            
    result += potion[minimum[0]]

    for [j, k] in sale[minimum[0]]:
        potion[j] -= k
        if potion[j] < 1:
            potion[j] = 1
    visited[minimum[0]] = True

print(result)            

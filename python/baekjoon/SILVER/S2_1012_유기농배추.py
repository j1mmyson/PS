import sys

sys.setrecursionlimit(3000)

def sol(arr):
    def dfs(x, y):
        if x<0 or y<0 or x >= len(arr) or y >= len(arr[0]) or arr[x][y] != 1:
            return
        arr[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                dfs(i, j)
                count += 1
    return count 

testCase = int(input())
for i in range(testCase):
    m, n, k = map(int, input().split())
    arr = [[0]*n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    print(sol(arr))
    
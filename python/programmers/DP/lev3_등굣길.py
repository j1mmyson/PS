# 프로그래머스 동적계획법(DP) 3단계 등굣깃
def solution(m, n, puddles):
    arr = [[1]*m for _ in range(n)]
    
    for i in puddles:
        arr[i[1]-1][i[0]-1] = 0
        if i[0]-1 == 0:
            for k in range(i[1]-1, n):
                arr[k][0] = 0
        elif i[1]-1 == 0:
            for k in range(i[0]-1, m):
                arr[0][k] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != 0:
                arr [i][j] = arr[i-1][j] + arr[i][j-1]
    
    return arr[n-1][m-1] % 1000000007

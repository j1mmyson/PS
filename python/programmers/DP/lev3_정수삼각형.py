# 프로그래머스 동적계획법(DP) 3단계 정수삼각형
def solution(triangle):
    answer = 0
    h = len(triangle)
    for i in range(h-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
    answer = triangle[0][0]
    return answer

# problem link: https://programmers.co.kr/learn/courses/30/lessons/64061
# 카카오 개발자 2019 겨울 인턴십 문제

def matrixMult(A):
    row=len(A)
    col=len(A[0])    
    
    B = [[0 for row in range(row)]for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B
def solution(board, moves):
    
    answer = 0
    b = matrixMult(board)
    for i in range(len(b)):
        while(1):
            if b[i][0] == 0:
                b[i].remove(0)
            else:
                break
            
    print(b)
    basket = list()
    for i in moves:
        if len(b[i-1]) != 0:
            value = b[i-1][0]
            basket.append(value)
            b[i-1].remove(value)
            if len(basket) >= 2:
                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
        else:
            pass
    return answer

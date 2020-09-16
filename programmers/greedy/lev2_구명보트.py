# 무게한도가 존재하는 보트로 사람들을 옮길 수 있는 최소한의 횟수를 구하는 문제.

def solution(people, limit):
    
    end = 1
    start = 0
    boat = 0
    speople = sorted(people)
    while True:
        if end + start > len(speople):
            break
        sum = 0
        if end+start != len(speople):
            sum = speople[-end] + speople[start]
        else:
            boat = boat + 1
            break
        if sum <= limit :
            boat = boat + 1
            end = end + 1
            start = start + 1
        else:
            boat = boat + 1
            end = end + 1
        
            
    answer = boat
    return answer

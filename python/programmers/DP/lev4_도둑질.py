# 프로그래머스 동적계획법(DP) 4단계 도둑질
def solution(money):
    r1 = 0
    r2 = 0
    route1 = money[:-1]
    route2 = money[1:]
    
    route1[2] += route1[0]
    route2[2] += route2[0]
    
    for i in range(3, len(route1)):
        route1[i] += max(route1[i-3], route1[i-2])
        route2[i] += max(route2[i-3], route2[i-2])
    
    r1 = max(route1[-1], route1[-2])
    r2 = max(route2[-1], route2[-2])
    return max(r1, r2)

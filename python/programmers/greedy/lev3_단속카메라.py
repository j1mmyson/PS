def solution(routes):
    answer = 1
    routes.sort()
    coverage = routes[0][1]
    
    for start, end in routes:
        if coverage >= start:
            coverage = min(end, coverage)      
        else:            
            coverage = end
            answer += 1

    return answer

def solution(clothes):
    answer = 1
    d = {}
    
    for c in clothes:
        if c[1] in d:
            d[c[1]] += 1
        else:
            d[c[1]] = 2
    
    l = d.values()
    
    for i in l:
        answer = answer * i
    
    return answer-1

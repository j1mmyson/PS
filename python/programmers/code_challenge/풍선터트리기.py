def solution(balloon):
    answer = 0
    l = len(balloon)
    left = [0 for _ in range(l)]
    right = [0 for _ in range(l)]
    lm = 1000000000
    rm = 1000000000
    
    for i in range(0, l):
        if balloon[i] < lm:
            lm = balloon[i]
        left[i] = lm
        
        
    for i in range(l-1, -1, -1):
        if balloon[i] < rm:
            rm = balloon[i]
        right[i] = rm
    
    
    for i in range(l):
        if balloon[i] <= left[i] or balloon[i] <= right[i]:
            answer += 1
    return answer
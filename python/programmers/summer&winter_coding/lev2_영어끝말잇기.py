def solution(n, words):
    
    turn = 1
    
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or (words[i] in words[:i-1]):
            return [n if (i+1)%n == 0 else (i+1)%n , turn]
        if (i+1) % n == 0:
            turn += 1
    
    return [0, 0]
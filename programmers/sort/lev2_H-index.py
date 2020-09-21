def solution(citations):
    answer = 0
    ind = 0
    n = len(citations)
    citations.sort()
    for i in reversed(range(n+1)):
        for item in citations:
            if i <= item:
                ind = citations.index(item)
                if n - ind >= i and ind <= i:
                    return i
            
    return 0

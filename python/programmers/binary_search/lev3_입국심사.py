def solution(n, times):
    left = 0
    right = n * max(times)
    answer = 0
    
    while(left <= right):
        mid = (left + right) // 2
        people = 0
        
        for i in times:
            people += mid//i
        
        if n > people:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer
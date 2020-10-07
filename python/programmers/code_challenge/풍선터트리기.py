def solution(a):
    answer = 2
    l = len(a)
    start = 0
    end = l-1
    left = a[0]
    right = [a[-1]]
    for i in range(l-1, 1, -1):
        if a[i] < right[-1]:
            right.append(a[i])
    for i in range(1,l-2):
        if (a[i]<left) or (a[i]<right[-1]):
            answer += 1
        if a[i] < left:
            left = a[i]
        if a[i+1] == right[-1]:
            right.pop()
    
    if a[-3] < left:
        left = a[-3]
    if a[-2] < right[-1]:
        right.pop()
    if len(right) == 0:
        answer+=1
    elif (a[-2]<left) or (a[-2]<right[-1]):
        answer += 1
    
            
    return answer

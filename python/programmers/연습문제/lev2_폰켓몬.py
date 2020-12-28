def solution(nums):
    answer = list()
    
    for i in nums:
        if i not in answer:
            answer.append(i)
    
    return min(len(nums)/2, len(answer))
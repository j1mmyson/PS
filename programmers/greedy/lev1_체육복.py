# 체육복을 도둑맞은 학생, 여분체육복이 있는 학생 목록을 받아와 체육복을 입을 수 있는 학생 수를 반환하는 함수 solution.

import copy
def solution(n, lost, reserve):
    if len(lost) == 0:
        return n
    answer = [1 for i in range(n+1)]
    lost.sort()
    reserve.sort()
    cp_lost = copy.deepcopy(lost)
    cp_reserve = copy.deepcopy(reserve)
    
    for i in lost:
        if i in reserve:
            cp_lost.remove(i)
            cp_reserve.remove(i)
    lost = copy.deepcopy(cp_lost)
    reserve = copy.deepcopy(cp_reserve)
    
    if len(lost) == 0:
        return n
    
    
    for i in reserve:
        if (i-1) not in lost:
            if (i+1) not in lost:
                cp_reserve.remove(i)
        elif (i-1) in lost:
            if (i+1) not in lost:
                cp_lost.remove(i-1)
                cp_reserve.remove(i)
        elif (i+1) in lost:
            if (i-1) not in lost:
                cp_lost.remove(i+1)
                cp_reserve.remove(i)

    
    lost = copy.deepcopy(cp_lost)
    reserve = copy.deepcopy(cp_reserve)
    
    for i in reserve:
        if (i-1) in lost:
            cp_lost.remove(i-1)
            cp_reserve.remove(i)
            lost = copy.deepcopy(cp_lost)
            reserve = copy.deepcopy(cp_reserve)
        elif (i+1) in lost:
            cp_lost.remove(i+1)
            cp_reserve.remove(i)
            lost = copy.deepcopy(cp_lost)
            reserve = copy.deepcopy(cp_reserve)
        
                
    lost = copy.deepcopy(cp_lost)
    reserve = copy.deepcopy(cp_reserve)
    
    for i in lost:
        answer[i] = 0
    
     
    return sum(answer) - 1

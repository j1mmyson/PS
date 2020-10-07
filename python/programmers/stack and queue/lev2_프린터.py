# 우선순위가 매겨진 인쇄목록 중에서 내가 출력하려는 인쇄물이 몇번째에 출력되는지 구하는 함수 solution.

import copy
def solution(priorities, location):
    answer = 1
    while(1):
        if len(priorities) == 1:
            return answer
        if location == 0:
            if priorities[0] >= max(priorities[1:]):
                return answer
            else:
                location = len(priorities)-1
                value = priorities.pop(0)
                priorities.append(value)
        else:
            if priorities[0] >= max(priorities[1:]):
                answer += 1
                priorities.pop(0)
                location -= 1
            else:
                value = priorities.pop(0)
                priorities.append(value)
                location -= 1
            
    return answer

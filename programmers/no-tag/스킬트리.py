# problem link: https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        ind = 0
        temp =""
        for st in i:
            if st in skill:
                temp = temp + st
        print(temp)
        can = 1
        for st in temp:
            s_ind = skill.index(st)
            st_ind = temp.index(st)
            if skill[0:s_ind] not in temp[0:st_ind]:
                can = 0
        
        if can == 1:
            answer = answer + 1
    
    return answer

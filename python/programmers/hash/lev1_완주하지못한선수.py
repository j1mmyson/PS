# 참여자와 완주자 목록을 받아와 완주하지 못한 선수를 반환해주는 함수 solution

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
        if i == len(participant)-1:
            return participant[i]
        if participant[i] != completion[i]:
            return participant[i]

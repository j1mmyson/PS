def solution(answers):
    answer = []
    a_a = [1,2,3,4,5]
    b_a = [2,1,2,3,2,4,2,5]
    c_a = [3,3,1,1,2,2,4,4,5,5]
    a_point = 0
    b_point = 0
    c_point = 0
    
    for i in range(len(answers)):
        if answers[i] == a_a[i%5]:
            a_point += 1
        if answers[i] == b_a[i%8]:
            b_point += 1
        if answers[i] == c_a[i%10]:
            c_point += 1
    maxmax = a_point
    if b_point > maxmax:
        maxmax = b_point
    if c_point > maxmax:
        maxmax = c_point
    
    if maxmax == a_point:
        answer.append(1)
    if maxmax == b_point:
        answer.append(2)
    if maxmax == c_point:
        answer.append(3)
    return answer

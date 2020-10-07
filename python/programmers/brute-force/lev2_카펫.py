def solution(brown, yellow):
    sum_ = 0
    can = []
    sum_ = brown + yellow
    for i in range(1, sum_):
        if sum_ % i == 0:
            can.append(i)
    
    for i in can:
        for j in can:
            if sum_ == i*j:
                if i >= j and (i-2)*(j-2) == yellow:
                    answer = [i,j]

    return answer

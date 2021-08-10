def getScore(score):
    n = score//10
    if n >= 9:
        return 'A'
    elif n == 8:
        return 'B'
    elif n == 7:
        return 'C'
    elif n >= 5:
        return 'D'
    return 'F'


def solution(scores):
    avg = []
    
    for stdNum in range(len(scores)):
        myScore = scores[stdNum][stdNum]
        temp = []
        
        for i in range(len(scores)):
            if i != stdNum:
                temp.append(scores[i][stdNum])
        if myScore > max(temp) or myScore < min(temp):
            avg.append(getScore(sum(temp)//len(temp)))
        else:
            avg.append(getScore((sum(temp)+myScore) // (len(temp)+1)))
    
    return "".join(avg)
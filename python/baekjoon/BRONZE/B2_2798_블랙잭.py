n, goal = map(int, input().split())

cardList = list(map(int, input().split()))
l = len(cardList)
s = 0
answer = 0
for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            s = cardList[i]+cardList[j]+cardList[k]
            if goal - s < 0:
                continue
            if goal-answer > goal-s:
                answer = s

print(answer)
length = int(input())
scoreList = input().split(' ')

for i in range(length):
    scoreList[i] = int(scoreList[i])

maxScore = max(scoreList)

for i in range(length):
    scoreList[i] = scoreList[i]/maxScore*100

answer = sum(scoreList) / len(scoreList)

print(answer)
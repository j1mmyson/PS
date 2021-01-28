numList = input().split(' ')

for i in range(len(numList)):
    numList[i] = int(numList[i]) * int(numList[i])

answer = sum(numList) % 10

print(answer)
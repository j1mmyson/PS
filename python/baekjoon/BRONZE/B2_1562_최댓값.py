numList = []
for i in range(9):
    numList.append(int(input()))

maxNum = max(numList)

for i, v in enumerate(numList):
    if maxNum == v:
        answer = i
        break

print(maxNum)
print(i+1)
numA, numB = input().split(' ')
numA = int(numA[::-1])
numB = int(numB[::-1])

if numA > numB:
    print(numA)
else:
    print(numB)

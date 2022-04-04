import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    n = int(sys.stdin.readline())
    sticker = []
    result = 0
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    
    if n == 1:
        result = max(sticker[0][0], sticker[1][0])
    elif n == 2:
        result = max(sticker[0][0] + sticker[1][1], sticker[0][1] + sticker[1][0])
    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        
        for j in range(2, n):
            for i in range(2):
                if i == 0:
                    sticker[i][j] = max(sticker[1][j-1], sticker[1][j-2]) + sticker[i][j]
                else:
                    sticker[i][j] = max(sticker[0][j-1], sticker[0][j-2]) + sticker[i][j]
        result = max(sticker[0][-1], sticker[1][-1])

    print(result)
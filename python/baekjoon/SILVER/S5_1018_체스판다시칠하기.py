row, col = map(int, input().split(' '))
board = []
minimum = 64

for i in range(row):
    board.append(input())

maxRow, maxCol = row-7, col-7

for i in range(maxRow):
    for j in range(maxCol):
        gap1 = 0
        gap2 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c)%2 == 0:
                    if board[r][c] != 'W':
                        gap1 += 1
                    if board[r][c] != 'B':
                        gap2 += 1
                else:
                    if board[r][c] != 'B':
                        gap1 += 1
                    if board[r][c] != 'W':
                        gap2 += 1
        minimum = min(minimum, gap1, gap2)
        
print(minimum)
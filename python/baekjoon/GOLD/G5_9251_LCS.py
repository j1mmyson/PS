import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

row = len(s1)
col = len(s2)

lcs = [[0]*(col+1) for i in range(row+1)]
m = 0

for i in range(row+1):
    for j in range(col+1):
        if i == 0 or j == 0:
            lcs[i][j] = 0
            continue
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1 
        else:
            if i > 0 and j > 0:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])
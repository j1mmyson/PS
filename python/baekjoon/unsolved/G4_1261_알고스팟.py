# 다익스트라 알고리즘으로 풀어야함. / 실패

import sys

miro = []
[m, n] = sys.stdin.readline().rstrip().split(' ')
m, n = int(m), int(n)
for i in range(int(n)):
    arr = sys.stdin.readline().rstrip()
    temp = []
    for i in arr:
        temp.append(int(i))
    miro.append(temp)


for m in range(1, m):
    miro[0][m] += miro[0][m-1]

for n in range(1, n):
    miro[n][0] += miro[n-1][0]

for i in range(1, m+1):
    for j in range(1, n+1):
        miro[j][i] += min(miro[j-1][i], miro[j][i-1])

print(miro[n][m])


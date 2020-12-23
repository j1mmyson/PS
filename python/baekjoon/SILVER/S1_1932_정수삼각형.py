import sys
n = int(input())

tra = []
for i in range(n):
    tra.append([])
    tra[i]=list(map(int, sys.stdin.readline().rstrip().split(' ')))


for i in range(n-2, -1, -1):
    k = i
    for j in range(k+1):
        tra[i][j] += max(tra[i+1][j], tra[i+1][j+1])

print(tra[0][0])
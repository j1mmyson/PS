# problem link: https://www.acmicpc.net/problem/15903

n, m = input().split()
n = int(n)
m = int(m)
num = []
num = list(map(int, input().split()))
summ = 0
num = sorted(num)

for i in range(m):
  summ = num[0] + num[1]
  num[0] = summ
  num[1] = summ
  num = sorted(num)

print(sum(num))
    

a = int(input())
b = int(input())
c = int(input())

answer = [0]*10

num = str(a*b*c)

for i in num:
    answer[int(i)] += 1

for i in answer:
    print(i)
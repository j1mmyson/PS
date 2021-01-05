n = int(input())

answer = input()
l = len(answer)

for i in range(n-1):
    val = input()
    temp = ''
    for i in range(l):
        if answer[i] != val[i]:
            temp += '?'
        else:
            temp += answer[i]
    answer = temp

print(answer)

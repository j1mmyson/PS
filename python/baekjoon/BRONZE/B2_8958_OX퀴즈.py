loop = int(input())

answer = []

for i in range(loop):
    quiz = input()
    temp = 0
    stack = 0
    for j in quiz:
        if j == 'O':
            stack += 1
            temp += stack
        else:
            stack = 0
        
    answer.append(temp)

for i in answer:
    print(i)
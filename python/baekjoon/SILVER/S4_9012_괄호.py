def checkVPS(text):
    stack = 0
    for i in text:
        if i == '(':
            stack += 1
        elif i == ')':
            if stack == 0:
                return False
            stack -= 1
    if stack == 0:
        return True
    return False

n = int(input())
for i in range(n):
    if checkVPS(input()) == False:
        print("NO")
    else:
        print("YES")

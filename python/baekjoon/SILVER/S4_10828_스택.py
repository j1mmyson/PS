import sys

input()
data = sys.stdin.read().splitlines()

stack = []

for i in data:
    cmd = i.split()[0]
    if cmd == "push":
        stack.append(int(i.split()[1]))
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
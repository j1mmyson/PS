import sys

input()
data = sys.stdin.read().splitlines()

que = []

for i in data:
    cmd = i.split()[0]
    if cmd == "push":
        que.append(int(i.split()[1]))
    elif cmd == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
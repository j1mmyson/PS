import sys

input()
data = sys.stdin.read().splitlines()

deque = []

for i in data:
    cmd = i.split()[0]
    if cmd == "push_back":
        deque.append(int(i.split()[1]))
    elif cmd == "push_front":
        deque.insert(0, int(i.split()[1]))
    elif cmd == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif cmd == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
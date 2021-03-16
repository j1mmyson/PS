import sys

n = int(input())

l = set()

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if "add" in cmd:
        v = int(cmd[4:])
        if v not in l:
            l.add(v)
    elif "remove" in cmd:
        v = int(cmd[7:])
        l.discard(v)
    elif "check" in cmd:
        v = int(cmd[6:])
        if v in l:
            print(1)
        else:
            print(0)
    elif "toggle" in cmd:
        v = int(cmd[7:])
        if v in l:
            l.remove(v)
        else:
            l.add(v)
    elif "all" in cmd:
        l = set([i for i in range(1, 21)])
    else:
        l = set()
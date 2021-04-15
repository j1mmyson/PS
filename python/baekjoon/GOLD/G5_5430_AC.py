import sys
from collections import deque

testCase = int(input())

for _ in range(testCase):
    func = sys.stdin.readline().rstrip()
    func = func.replace("RR", "")
    l = int(input())
    case = sys.stdin.readline().rstrip()[1:-1].split(',')
    d = -1
    if case == ['']:
        case = []
    else:
        case = deque(case)
    
    if len(case) < func.count('D'):
        print("error")
    else:
        for f in func:
            if f == 'R':
                d *= -1
            else:
                if d == -1:
                    case.popleft()
                else:
                    case.pop()
        if d == -1:
            print("[" + ",".join(list(case)) + "]")
        else:
            print("[" + ",".join(list(case)[::-1]) + "]")


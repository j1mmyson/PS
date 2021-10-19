def turnGear(gear, wise):
    if wise == 0:
        return gear
    elif wise == 1:
        gear = [gear[-1]] + gear[:-1]
    else:
        gear = gear[1:] + [gear[0]]
    
    return gear

import sys

gear = []

for _ in range(4):
    gear.append(list(map(int, list(sys.stdin.readline().strip()))))

n = int(input())

for _ in range(n):
    gearNum, direct = map(int, sys.stdin.readline().split())
    gearNum -= 1
    d = [0, 0, 0, 0]
    
    if gearNum == 0:
        seq = [1, 2, 3]
        crt = [0, 1, 2]
    elif gearNum == 1:
        seq = [0, 2, 3]
        crt = [1, 1, 2]
    elif gearNum == 2:
        seq = [1, 0, 3]
        crt = [2, 1, 2]
    else:
        seq = [2, 1, 0]
        crt = [3, 2, 1]
    d[gearNum] = direct
    for i in range(3):
        if seq[i] > crt[i]:
            if gear[seq[i]][6] == gear[crt[i]][2]:
                d[seq[i]] = 0
            else:
                d[seq[i]] = d[crt[i]] * -1
        else:
            if gear[seq[i]][2] == gear[crt[i]][6]:
                d[seq[i]] = 0
            else:
                d[seq[i]] = d[crt[i]] * -1

    for i in range(4):
        gear[i] = turnGear(gear[i], d[i])

answer = 0
v = 1
for i in range(4):
    if gear[i][0] == 1:
        answer += v
    v *= 2

print(answer)
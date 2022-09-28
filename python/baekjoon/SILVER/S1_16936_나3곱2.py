import sys
import copy

n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
s2 = set(num_list)


answer = []

for num in num_list:
    answer = [num]
    s1 = copy.deepcopy(s2)

    for i in range(n):
        current = answer[-1]
        if (current // 3) in s1 and current % 3 == 0:
            temp = current // 3
            answer.append(temp)
            s1.remove(temp)
        elif current * 2 in s1:
            temp = current * 2
            answer.append(temp)
            s1.remove(temp)

    if len(answer) == n:
        print(*answer)
        break




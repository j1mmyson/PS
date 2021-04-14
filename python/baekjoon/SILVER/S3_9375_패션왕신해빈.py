import sys

testCase = int(input())

for _ in range(testCase):
    d = {}
    n = int(input())
    for _ in range(n):
        item, part = sys.stdin.readline().split()
        if d.get(part):
            d[part].append(item)
        else:
            d[part] = [item]
    key_list = d.keys()
    temp = 1
    for i in key_list:
        temp = temp * (len(d[i]) + 1)
    print(temp-1)
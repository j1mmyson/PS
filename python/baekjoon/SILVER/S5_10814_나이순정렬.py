d = {}

n = int(input())

for i in range(n):
    inp = input().split()
    age, name = int(inp[0]), inp[1]
    if d.get(age):
        d[age].append(name)
    else:
        d[age] = [name]

new_list = sorted(d.items())

for l in new_list:
    for i in range(len(l[1])):
        print(l[0], l[1][i])
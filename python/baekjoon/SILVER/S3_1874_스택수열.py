import sys

def check(l):
    maxValue = l[0]

    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            if maxValue > l[i+1]:
                return False
            else:
                maxValue = l[i+1]
    return True


n = int(input())
ind = 0
temp = [1]
num = 2

l = []


for i in range(n):
    l.append(int(sys.stdin.readline()))

if check(l):
    print("+")
    while ind != n:
        if not temp:
            temp.append(num)
            num += 1
            print("+")
        elif l[ind] != temp[-1]:
            temp.append(num)
            num += 1
            print("+")
        else:
            ind += 1
            temp.pop()
            print("-")
else:
    print("NO")

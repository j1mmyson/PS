import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))
res = [-1] * n

p = 1
for i in l:
    ind = 0
    if i == 0:
        while res[ind] != -1:
            ind += 1
    else:
        count = 0
        while True:
            if res[ind] == -1:
                if count == i:
                    break
                else:
                    count += 1
                    ind += 1
            else:
                ind += 1
            

    res[ind] = p
    p += 1

for i in res:
    print(i, end=' ')
print()

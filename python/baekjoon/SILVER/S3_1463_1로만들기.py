n = int(input())

arr = [0, 0]

for i in range(2, n+1):
    l = []
    if i%3 == 0:
        l.append(arr[i//3])
    if i%2 == 0:
        l.append(arr[i//2])
    l.append(arr[i-1])
    
    arr.append(min(l)+1)

print(arr[n])

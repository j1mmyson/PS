import heapq
n = int(input())

arr = [1, 1]

for i in range(2, n+1):
    k = 1
    kgroup = []
    while k <= i//2:
        kgroup.append(2 * arr[i-k] - arr[i-2*k])
        k += 1
    num = 1
    while True:
        if num not in kgroup:
            arr.append(num)
            break
        num += 1

print(arr[-1])

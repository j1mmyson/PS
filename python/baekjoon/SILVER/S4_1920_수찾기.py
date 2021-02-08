# def BSearch(target, data):
#     data.sort()
#     start = 0
#     end = len(data)-1

#     while start <= end:
#         mid = (start + end)//2

#         if data[mid] == target:
#             return mid
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None

def BSearch(target, start, end, data):
    if start > end:
        return None
    mid = (start + end)//2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    
    return BSearch(target, start, end, data)

input()
m = list(map(int, input().split(' ')))
m.sort()
input()
n = list(map(int, input().split(' ')))

for i in n:
    v = BSearch(i, 0, len(m)-1, m)
    if v == None:
        print(0)
    else:
        print(1)
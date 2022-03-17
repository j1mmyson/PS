import heapq, sys

# def heap_sort(nums):
#     heap = []
#     for num in nums:
#         heapq.heappush(heap, num)
#     sorted_nums = []
#     while heap:
#         sorted_nums.append(heapq.heappop(heap))
#     return sorted_nums

def solution(operations):
    maxheap = []
    minheap = []
    checkLen = 0
    visited = [False] * len(operations)

    for [i, item] in enumerate(operations):
        op, num = item.split()
        num = int(num)

        if op == 'I':
            heapq.heappush(minheap, (num, i))
            heapq.heappush(maxheap, (-num, i))
            visited[i] = True
            checkLen += 1
        elif checkLen == 0:
            continue
        else:
            if num == 1:
                while maxheap and visited[maxheap[0][1]] == False:
                    heapq.heappop(maxheap)
                if checkLen > 0:
                    visited[maxheap[0][1]] = False
                    heapq.heappop(maxheap)
                    checkLen -= 1

            else:
                while minheap and visited[minheap[0][1]] == False:
                    heapq.heappop(minheap)
                if checkLen > 0:
                    visited[minheap[0][1]] = False
                    heapq.heappop(minheap)
                    checkLen -= 1

    if checkLen == 0:
        return "EMPTY"
    
    while maxheap and visited[maxheap[0][1]] == False:
        heapq.heappop(maxheap)

    while minheap and visited[minheap[0][1]] == False:
        heapq.heappop(minheap)
    
    return str(-1 * heapq.heappop(maxheap)[0]) + ' ' + str(heapq.heappop(minheap)[0])


n = int(input())

for _ in range(n):
    op = []
    i = int(input())
    for _ in range(i):
        op.append(sys.stdin.readline())
    print(solution(op))

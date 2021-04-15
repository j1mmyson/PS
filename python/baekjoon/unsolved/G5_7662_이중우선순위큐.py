import heapq, sys

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

def solution(operations):
    heap = []
    for item in operations:
        if "I " in item:
            item = item.replace("I ", "")
            value = int(item)
            heapq.heappush(heap, value)
        elif len(heap) == 0:
            pass
        elif "D -" in item:
            heap = heap_sort(heap)
            heap.pop(0)
        else:
            heap = heap_sort(heap)
            heap.pop(-1)
            
    heap = heap_sort(heap)
    if len(heap) == 0:
        return "EMPTY"
    return str(heap[-1]) + " " +str(heap[0])

n = int(input())
# answer = []
for _ in range(n):
    op = []
    i = int(input())
    for _ in range(i):
        op.append(sys.stdin.readline())
    print(solution(op))

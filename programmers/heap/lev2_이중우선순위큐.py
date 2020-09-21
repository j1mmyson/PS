import heapq
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
        return [0,0]
    else:
        return [heap[-1], heap[0]]
    
    return heap

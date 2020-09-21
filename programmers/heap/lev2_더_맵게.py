import heapq
import copy

def solution(scoville, K):
    heap = []
    a = 0
    b = 0
    value = 0
    answer = 0
    
    heapq.heapify(scoville)
    
    while(True):
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
        a = copy.deepcopy(heapq.heappop(scoville))
        if a >= K:
            break
        b = copy.deepcopy(heapq.heappop(scoville))
        value = a + 2*b
        answer += 1
        heapq.heappush(scoville, value)
    return answer

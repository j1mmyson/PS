import sys
import heapq

n = int(input())

for _ in range(n):
    s, k = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    
    start, end = 0, 0
    answer = 0
    temp = 2 * (10**8)

    while True:
        if start + end == s-1:
            break
        t = l[start] + l[-end-1]
        v = abs(k - t)
        
        if v == temp:
            answer += 1
        else:
            if temp > v:
                temp = v
                answer = 1
        if l[start] + l[-end-1] > k:
            end += 1
        else:
            start += 1  
    print(answer)






    # hq = []
    # for i in range(s-1):
    #     for j in range(i+1, s):
    #         v = abs(k - l[i] - l[j] )
    #         heapq.heappush(hq, v)
    
    # temp = heapq.heappop(hq)
    # answer = 1
    # while True:
    #     if heapq.heappop(hq) != temp:
    #         break
    #     answer += 1
    # print(answer)

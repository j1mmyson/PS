import sys

def makeNew(current, n):
    board=[]
    can = set(i for i in range(n))
    loc = len(current)
    ind = 0
    for i in current:
        can.discard(i)
        gap = loc - ind
        can.discard(i-gap)
        can.discard(i+gap)
        ind += 1

    for i in range(n):
        if i in can:
            board.append(current + [i])
    return board


def nQueen(n):
    answer = 0
    q = []
    for i in range(n):
        q.append([i])
    
    while q:
        current = q.pop()
        if len(current) == n:
            answer += 1
            continue
        q.extend(makeNew(current, n))
    return answer


n = int(sys.stdin.readline())

print(nQueen(n))




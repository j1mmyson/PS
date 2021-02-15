def roomNo(w, h, p):
    W, H = 1, 0
    while(True):
        if p <= h:
            break
        p = p - h

        W += 1
    
    H = p
    return W, H


n = int(input())

for i in range(n):
    h, w, p = map(int, input().split())
    W, H = roomNo(w,h,p)
    if W < 10:
        print(H,0,W, sep='')
    else:
        print(H,W, sep='')

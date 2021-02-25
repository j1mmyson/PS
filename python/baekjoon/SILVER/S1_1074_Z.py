
n, r, c = map(int, input().split())

answer = 0
n = pow(2, n)

while(n!=1):
    n = n // 2
    if r<n and c<n:
        pass
    elif r<n and c>=n:
        answer += pow(n, 2)
    elif r>=n and c<n:
        answer += 2*pow(n, 2)
    else:
        answer += 3*pow(n, 2)
    r = r%n
    c = c%n
print(answer)

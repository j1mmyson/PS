n = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
answer = 0

while True:
    if n == 0:
        break
    for s in stick:
        if n >= s:
            n = n - s
            answer += 1

print(answer)
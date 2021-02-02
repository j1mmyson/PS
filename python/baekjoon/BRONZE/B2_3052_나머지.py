answer = []

for i in range(10):
    num = int(input())
    if num%42 not in answer:
        answer.append(num%42)

print(len(answer))
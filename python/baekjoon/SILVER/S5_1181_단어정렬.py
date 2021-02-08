num = int(input())

answer = []
for i in range(num):
    val = input()
    if val not in answer:
        answer.append(val)

answer.sort(key=lambda x: (len(x), x))

for i in answer:
    print(i)
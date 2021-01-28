word = input().upper()
answer = ' '
d = {}

for i in word:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1


maxVal = max(d.values())

for key, val in d.items():
    if val == maxVal:
        if answer == ' ':
            answer = key
        else:
            answer = '?'
            break

print(answer)
    
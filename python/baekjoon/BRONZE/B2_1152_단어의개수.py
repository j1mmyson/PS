word = input().strip()
answer = 1
print(word)

for i in range(len(word)-1):
    if (word[i] == ' ') and (word[i+1] != ' '):
        answer = answer + 1

print(answer)
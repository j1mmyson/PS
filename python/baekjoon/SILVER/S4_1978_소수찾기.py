def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num < 2:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

answer = 0
input()
numList = map(int, input().split(' '))

for i in numList:
    if isPrime(i) is True:
        answer += 1

print(answer)

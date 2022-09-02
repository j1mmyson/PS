def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n < 2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    
    return True


def convert(n, k):
    base = ''

    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)

    return base[::-1]


def solution(n, k):
    answer = 0
    converted_number = convert(n, k)

    num = ''
    for i in range(len(converted_number)):
        if converted_number[i] == '0':
            if num == '':
                continue
            if isPrime(int(num)):
                answer += 1
            num = ''
        elif i == len(converted_number) - 1:
            num += converted_number[i]
            if isPrime(int(num)):
                answer += 1
            num = ''
        else:
            num += converted_number[i]

    return answer


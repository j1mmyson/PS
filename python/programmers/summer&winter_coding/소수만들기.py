def checkPrime(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    return isPrime
        

def solution(nums):
    answer = 0
    num = []
    num2 = []

    for i, v1 in enumerate(nums):
        num = nums[i+1:]
        for j, v2 in enumerate(num):
            num2 = num[j+1:]
            for k, v3 in enumerate(num2):
                if checkPrime(v1+v2+v3):
                    answer += 1
    return answer

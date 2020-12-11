def solution(n):
    num1 = 1
    num2 = 2
    
    for _ in range(n-2):
        num1, num2 = num2, num1+num2

    return num2 % 1000000007

def solution(number, k):
    s = 0
    for i in range(k): # k번 숫자를 뺀다
        for j in range(s, len(number)-1):
            l = len(number)
            if j == l-1:
                number = number[:-1]
                break
            elif number[j] < number[j+1]:
                number = number[0:j]+number[j+1:]
                break
    return number
# 75/100점 나온다.. 7, 10번 케이스 시간초과/ 12번케이스 실패

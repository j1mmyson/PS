def getCount(count):
    return count * (count+1) / 2

def solution(price, money, count):

    answer = price * getCount(count) - money

    return answer if answer >= 0 else 0
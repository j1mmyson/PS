def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                print(phone_book[i], phone_book[j])
                return False
    return answer

def check(s):
    before = s
    temp = ""
    while True:
        before = s
        s = s.replace("[]", "")
        s = s.replace("()", "")
        s = s.replace("{}", "")
        after = s
        if before == after:
            break
    if s:
        return False
    
    return True
        

def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            answer += 1
    return answer
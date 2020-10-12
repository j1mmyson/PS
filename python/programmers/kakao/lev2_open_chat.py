def solution(record):
    d = {}
    E = 'Enter'
    L = 'Leave'
    C = 'Change'

    result = []

    for i in record:
        sp = i.split()
        sp[1] = sp[1].replace('uid', '')
        if sp[0] == E:
            d[sp[1]] = sp[2]
        elif sp[0] == C:
            d[sp[1]] = sp[2]

    for i in record:
        sp = i.split()
        sp[1] = sp[1].replace('uid', '')
        if sp[0] == E:
            temp = d[sp[1]] + "님이 들어왔습니다."
            result.append(temp)
        elif sp[0] == L:
            temp = d[sp[1]] + "님이 나갔습니다."
            result.append(temp)

    return result

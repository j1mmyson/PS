def solution(new_id):
    # 1
    new_id = new_id.lower() 
    # 2
    temp = ""
    for j in new_id:
        if ('a' <= j) and ('z' >= j ) or (j in ['-', '_', '.']) or (j in ['1', '2', '3', '4', '5', '6', '7','8','9','0']):
            temp = temp + j
    new_id = temp
    # 3
    temp = ""
    for j in range(1, len(new_id)):
        if new_id[j] != '.':
            temp = temp + new_id[j]
        elif new_id[j-1] != '.':
            temp = temp + new_id[j]
    new_id = new_id[0] + temp
    #4
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    #5
    if len(new_id) == 0:
        new_id = 'a'
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    #7
    while(True):
        if len(new_id) >= 3:
            break
        new_id = new_id + new_id[-1]
    
    answer = new_id
    
    return answer

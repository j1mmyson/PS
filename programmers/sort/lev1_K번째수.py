def solution(array, commands):
    answer = []
    value = 0
    i = 0
    j = 0
    k = 0
    for command in commands:
        print(command)
        i = command[0]-1
        j = command[1]
        k = command[2]-1
        
        n_array = array[i:j]
        n_array.sort()
        value = n_array[k]
        answer.append(value)
    return answer

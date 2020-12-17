def dfs(depth, numbers, target, result):
    global count
    if depth == len(numbers)-1:
        if result + numbers[-1] == target or result - numbers[-1] == target:
            count += 1
            return
    else:
        dfs(depth + 1, numbers, target, result + numbers[depth])
        dfs(depth + 1, numbers, target, result - numbers[depth])

def solution(numbers, target):
    global count
    count = 0
    result = 0
    depth = 0

    dfs(depth, numbers, target, result)
    answer = count

    return answer
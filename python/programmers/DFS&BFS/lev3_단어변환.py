
def isNext(src, dst):
    cnt = 0
    for i in range(len(src)):
        if src[i] == dst[i]:
            cnt += 1
    if cnt == len(src)-1:
        return True
    return False

def dfs(depth, word, target, visited, words):
    global answer
    
    if word == target:
        answer = depth
        return
    
    for i in range(len(words)):
        if not visited[i] and isNext(word, words[i]):
            visited[i] = True
            dfs(depth+1, words[i], target, visited, words)
            visited[i] = False
    return

def solution(begin, target, words):
    global answer
    answer = len(words)
    visited = [False] * len(words)
    
    if target not in words:
        return 0
    dfs(0, begin, target, visited, words)
    return answer
def getSubset(lst):
    n = len(lst)
    ans = []
    val = ''
    ind = 0
    for i in range(1<<n):
        for j in range(n):
            t_f = i & (1 << j)
            if t_f:
                val += lst[j]
        if val !='':
            ans.append(int(val))
        else:
            ans.append(val)
        val = ''
    return ans

n = int(input())

if n >1022:
    print(-1)
else:    
    result = getSubset(['9','8', '7', '6', '5', '4', '3', '2', '1', '0'])
    result.pop(0)
    result = sorted(result)
    print(result[n])
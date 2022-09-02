def solution(id_list, report, k):
    dic = {}
    for r in set(report) :
        er, ed = r.split()
        if dic.get(ed):
            dic[ed][0] += 1
            dic[ed][1].append(er)
        else:
            dic[ed] = [1, [er]]

    answer = [0] * len(id_list)

    for x in dic.values():
        if x[0] >= k:
            for u in x[1]:
                answer[id_list.index(u)] += 1

    return answer

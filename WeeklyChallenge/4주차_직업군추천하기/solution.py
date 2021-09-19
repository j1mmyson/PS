def solution(table, languages, preference):
    answer = ''
    answerTable = []
    for t in table:
        tab = t.split()
        point = 0
        for i in range(len(languages)):
            try:
                point += (6 - tab.index(languages[i])) * preference[i]
            except:
                continue
        answerTable.append([tab[0], point])
    
    answerTable.sort(key=lambda x : (-x[1], x[0]))
        
    return answerTable[0][0]
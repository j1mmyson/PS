func solution(answers []int) (answer []int) {
    
    p1 := [5]int{1, 2, 3, 4, 5}
    p2 := [8]int{2,1,2,3,2,4,2,5}
    p3 := [10]int{3,3,1,1,2,2,4,4,5,5}
    
    a1 := 0
    a2 := 0
    a3 := 0
    
    l1 := len(p1)
    l2 := len(p2)
    l3 := len(p3)
    
    if p1[0] == answers[0]{
        a1 += 1
    }
    if p2[0] == answers[0]{
        a2 += 1
    }
    if p3[0] == answers[0]{
        a3 += 1
    }
    
    for i := 1; i<len(answers); i++{
        if p1[i%l1] == answers[i]{
            a1 += 1
        }
        if p2[i%l2] == answers[i]{
            a2 += 1
        }
        if p3[i%l3] == answers[i]{
            a3 += 1
        }
    }
    
    max := 0
    if a1 >= a2{
        max = a1
    }else{
        max = a2
    }
    if a3 >= max{
        max = a3
    }
    
    
    if a1 == max{
        answer = append(answer, 1)
    }
    if a2 == max{
        answer = append(answer, 2)
    }
    if a3 == max{
        answer = append(answer, 3)
    }
    return
}

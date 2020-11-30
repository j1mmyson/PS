func solution(clothes [][]string) (answer int) {
    answer = 1
    d := make(map[string]int)
    
    for _, v := range clothes{
        if _, exist := d[v[1]]; exist{
            d[v[1]] += 1
        }else{
            d[v[1]] = 2
        }
    }
    for _, val := range d{
        answer *= val
    }
    answer -= 1
    return
}

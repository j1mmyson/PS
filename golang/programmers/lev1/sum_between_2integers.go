func solution(a int, b int) int {
    if a == b{
        return a
    }else if a > b{
        temp := a
        a = b
        b = temp
    }
    sum := 0
    
    for i := a; i<=b ; i++{
        sum += i
    }
    
    return sum
}

func solution(brown int, yellow int) (answer []int) {
    sum := 0
    can := []int {}
    sum = brown + yellow
    
    for i:= 1;i<sum;i++{
        if sum % i == 0{
            can = append(can, i)
        }
    }
    for _, i:= range can{
        for _, j := range can{
            if sum == i*j{
                if i >= j && (i-2)*(j-2) == yellow{
                    answer = []int{i, j}
                    return
                }
            }
        }
    }
    return
}

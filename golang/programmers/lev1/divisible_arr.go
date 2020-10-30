import "sort"
func solution(arr []int, divisor int) (answer []int) {
    for _, v := range arr{
        if v % divisor == 0{
            answer = append(answer, v)
        }
    }
    if len(answer)==0{
        answer = append(answer, -1)
    }
    sort.Ints(answer)
    return 
}

import "strconv"
func solution(seoul []string) string {
    for i, value := range seoul{
        if value == "Kim"{
            answer := "김서방은 "+strconv.Itoa(i)+"에 있다"
            return answer
        }
    }
    return ""
}

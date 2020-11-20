import "strconv"

func solution(s string) bool {
    l := len(s)
    if l != 4 && l != 6 {
        return false
    }
    
    _, err := strconv.Atoi(s)
    
    if err != nil{
        return false
    }
    
    return true
}

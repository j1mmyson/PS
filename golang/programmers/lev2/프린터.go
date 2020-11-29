func max(arr []int) (m int){
    
    for _, v := range arr{
        if v >= m{
            m = v
        }
    }
    return
}
func solution(priorities []int, location int) (answer int) {
    v := 0
    answer = 1
    
    for{
        if len(priorities) == 1{
            return
        }
        
        if location == 0{
            if priorities[0] >= max(priorities[1:]){
                return
            }else{
                location = len(priorities)-1
                v, priorities = priorities[0], priorities[1:]
                priorities = append(priorities, v)
            }
        }else{
            if priorities[0] >= max(priorities[1:]){
                answer += 1
                _, priorities = priorities[0], priorities[1:]
                location -= 1
            }else{
                v, priorities = priorities[0], priorities[1:]
                priorities = append(priorities, v)
                location -= 1
            }
        }
    }
    return
}

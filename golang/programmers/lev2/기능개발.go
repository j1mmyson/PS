func solution(progresses []int, speeds []int) (answer []int) {
    answer = []int{}
    temp := 0
    for{
        if len(progresses) == 0{
            return
        }else if progresses[0] >= 100{
            for{
                if progresses[0] >= 100{
                    progresses = progresses[1:]
                    speeds = speeds[1:]
                    temp += 1
                    if len(progresses) == 0{
                        answer = append(answer, temp)
                        break
                    }
                }else{
                    answer = append(answer, temp)
                    temp = 0
                    break
                }
            }
        }else{
            for i, _ := range progresses{
                progresses[i] = progresses[i] + speeds[i]
            }
        }   
    }
    return
}

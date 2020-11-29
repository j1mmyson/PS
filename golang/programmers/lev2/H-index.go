import "sort"

func findInd(arr []int, value int) (i int){
    i = 0
    v := 0
    for i, v = range arr{
        if value == v{
            return
        }
    }
    return
}

func solution(citations []int) int {
    ind := 0
    n := len(citations)
    sort.Ints(citations)
    
    for i := n; i>=0; i--{
        for _, v := range citations{
            if i <= v{
                ind = findInd(citations, v)
                if n - ind >= i{
                    return i
                }
            }
        }
    }
    return 0
}

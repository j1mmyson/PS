package kata

func FindEvenIndex(arr []int) int {
	length := len(arr)
	fromLeft := []int{arr[0]}
	fromRight := []int{arr[length-1]}

	for i := 1; i < len(arr); i++ {
		fromLeft = append(fromLeft, arr[i]+fromLeft[len(fromLeft)-1])
		fromRight = append(fromRight, arr[length-i-1]+fromRight[len(fromRight)-1])
	}

	for i, v := range fromLeft {
		if v == fromRight[length-i-1] {
			return i
		}
	}
	return -1
}

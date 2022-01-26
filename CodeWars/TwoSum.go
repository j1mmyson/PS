package kata

func TwoSum(numbers []int, target int) [2]int {
	l := len(numbers)
	for i := 0; i < l-1; i++ {
		for j := i + 1; j < l; j++ {
			temp := numbers[i] + numbers[j]
			if temp == target {
				return [2]int{i, j}
			}
		}
	}

	return [2]int{-1, -1}
}

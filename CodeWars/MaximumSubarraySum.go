package kata

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func MaximumSubarraySum(numbers []int) (max int) {
	max = 0
	temp := 0
	l := len(numbers)

	for i := 0; i < l-1; i++ {
		temp = numbers[i]
		max = Max(max, temp)
		for j := i + 1; j < l; j++ {
			temp += numbers[j]
			max = Max(max, temp)
		}
	}
	return
}

package kata

func Between(a, b int) []int {
	numbers := make([]int, b-a+1)
	for i, _ := range numbers {
		numbers[i] = a + i
	}

	return numbers
}

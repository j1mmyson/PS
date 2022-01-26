package kata

import "math"

func SquareSum(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += int(math.Pow(float64(num), 2))
	}
	return sum
}

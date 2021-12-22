package kata

func Pyramid(n int) [][]int {
	pyramid := [][]int{}
	temp := []int{}
	for i := 0; i < n; i++ {
		temp = append(temp, 1)
		pyramid = append(pyramid, temp)
	}
	return pyramid
}

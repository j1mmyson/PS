package kata

func Parse(data string) []int {
	answer := []int{}
	num := 0

	for _, v := range data {
		switch rune(v) {
		case 'i':
			num += 1
		case 'd':
			num -= 1
		case 's':
			num = num * num
		case 'o':
			answer = append(answer, num)
		}
	}

	return answer
}

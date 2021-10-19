package kata

func Solution(str string) []string {
	result := []string{}

	if len(str)%2 != 0 {
		str += "_"
	}

	for len(str) != 0 {
		result = append(result, str[0:2])
		str = str[2:]
	}

	return result
}

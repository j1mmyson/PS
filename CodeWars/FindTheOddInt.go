package kata

func FindOdd(seq []int) int {
	numMap := make(map[int]bool)

	for _, v := range seq {
		_, exists := numMap[v]
		if exists {
			numMap[v] = !numMap[v]
		} else {
			numMap[v] = true
		}
	}

	for key, val := range numMap {
		if val == true {
			return key
		}
	}

	return 0
}

// 짝수번 XOR 되면 0으로 돌아오는 원리를 이용...ㄷㄷ
func CleverSolution(seq []int) int {
	res := 0
	for _, x := range seq {
		res ^= x
	}
	return res
}

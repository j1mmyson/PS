package solution

func minMaxFromArray(list []int) (int, int) {
	var smallest, biggest int
	smallest, biggest = list[0], list[0]
	for _, v := range list {
		if v > biggest {
			biggest = v
		}
		if v < smallest {
			smallest = v
		}
	}
	return smallest, biggest
}

func getAvg(list []int) int {
	var sum int
	sum = 0
	for _, v := range list {
		sum += v
	}

	return sum / len(list)
}

func solution(scores [][]int) string {
	m := map[int]rune{
		10: 'A',
		9:  'A',
		8:  'B',
		7:  'C',
		6:  'D',
		5:  'D',
		4:  'F',
		3:  'F',
		2:  'F',
		1:  'F',
		0:  'F',
	}

	var answer []int

	for i := 0; i < len(scores); i++ {
		myScore := scores[i][i]
		temp := []int{}
		for j := 0; j < len(scores); j++ {
			if j == i {
				continue
			}
			temp = append(temp, scores[j][i])
		}
		minimum, maximum := minMaxFromArray(temp)
		if myScore >= minimum && myScore <= maximum {
			temp = append(temp, myScore)
		}
		answer = append(answer, getAvg(temp))
	}

	result := ""
	for _, v := range answer {
		result += string(m[v/10])
	}
	return result
}

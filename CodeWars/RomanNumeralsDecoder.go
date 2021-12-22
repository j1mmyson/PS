package kata

func Decode(roman string) int {
	sum := 0
	roman += "="
	m := make(map[string]int)
	m["I"] = 1
	m["V"] = 5
	m["X"] = 10
	m["L"] = 50
	m["C"] = 100
	m["D"] = 500
	m["M"] = 1000

	for ind, word := range roman {
		if string(roman[ind+1]) == "=" {
			sum += m[string(word)]
			break
		}
		if m[string(roman[ind])] < m[string(roman[ind+1])] {
			sum -= m[string(word)]
		} else {
			sum += m[string(word)]
		}
	}
	return sum
}

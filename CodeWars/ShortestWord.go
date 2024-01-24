package kata

func FindShort(s string) int {
	shortestLength := len(s)
	count := 0
	for _, char := range s {
		if char == ' ' {
			if count < shortestLength {
				shortestLength = count
			}
			count = 0
		} else {
			count++
		}
	}

	if count < shortestLength {
		shortestLength = count
	}

	return shortestLength
}

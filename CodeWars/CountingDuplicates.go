package kata

import "strings"

func duplicate_count(s1 string) int {
	answer := 0
	m := make(map[rune]bool)
	s1 = strings.ToLower(s1)

	for _, letter := range s1 {
		if val, exists := m[letter]; !exists {
			m[letter] = false
		} else if val == false {
			m[letter] = true
			answer += 1
		}
	}

	return answer
}

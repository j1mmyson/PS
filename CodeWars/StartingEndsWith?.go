package kata

import "strings"

func solution(str, ending string) bool {
	l := len(str) - len(ending)
	if l < 0 {
		return false
	}
	if str[l:] == ending {
		return true
	}
	return false
}

func solution2(str, ending string) bool {
	return strings.HasSuffix(str, ending)
}

func solution3(str, ending string) bool {
	return len(str) >= len(ending) && str[len(str)-len(ending):] == ending
}

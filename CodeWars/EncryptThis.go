package kata

import (
	"strconv"
	"strings"
)

func EncryptThis(text string) string {
	words := strings.Fields(text)
	var temp string
	var length int
	var answer []string
	for _, word := range words {
		length = len(word)
		temp = strconv.Itoa(int(word[0]))

		if length == 1 {

		} else if length == 2 {
			temp += string(word[1])
		} else {
			temp += string(word[length-1]) + word[2:length-1] + string(word[1])
		}

		answer = append(answer, temp)
	}

	return strings.Join(answer, " ")
}

package kata

import "strings"

func DuplicateEncode(word string) string {
	word = strings.ToLower(word)
	dic := make(map[rune]string)
	for _, c := range word {
		if _, exists := dic[c]; exists {
			dic[c] = ")"
		} else {
			dic[c] = "("
		}
	}

	res := ""

	for _, c := range word {
		res += string(dic[c])
	}

	return res
}

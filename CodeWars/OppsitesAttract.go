package kata

func LoveFunc(flower1, flower2 int) bool {
	if (flower1^flower2)%2 == 1 {
		return true
	}
	return false
}

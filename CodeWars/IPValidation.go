package kata

import (
	"strconv"
	"strings"
)

func Is_valid_ip(ip string) bool {
	split := strings.Split(ip, ".")
	if len(split) != 4 {
		return false
	}

	for _, addr := range split {
		if strings.HasPrefix(addr, "0") && len(addr) != 1 {
			return false
		}

		v, err := strconv.Atoi(addr)
		if err != nil {
			return false
		}
		if v < 0 || v > 255 {
			return false
		}
	}

	return true
}

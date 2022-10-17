package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	t := scanner.Text()
	tc, _ := strconv.Atoi(t)

	for i := 0; i < tc; i++ {
		scanner.Scan()
		s := scanner.Text()
		var l bytes.Buffer
		var r bytes.Buffer

		for ind := 0; ind < len(s); ind++ {
			if ind%2 == 0 {
				l.WriteByte(s[ind])
			} else {
				r.WriteByte(s[ind])
			}
		}
		fmt.Printf("%s %s\n", l.String(), r.String())
	}
}

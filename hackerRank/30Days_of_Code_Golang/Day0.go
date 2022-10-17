package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Hello, World.")
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')

	fmt.Println(s)

	return
}

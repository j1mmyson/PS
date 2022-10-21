package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	m := make(map[string]string)
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	num, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < num; i++ {
		scanner.Scan()
		m[strings.Split(scanner.Text(), " ")[0]] = strings.Split(scanner.Text(), " ")[1]
	}

	for scanner.Scan() {
		val, exists := m[scanner.Text()]
		if !exists {
			fmt.Println("Not found")
		} else {
			fmt.Printf("%s=%s\n", scanner.Text(), val)
		}
	}
}

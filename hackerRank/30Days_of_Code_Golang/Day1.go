package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".

	var i uint64 = 4
	var d float64 = 4.0
	var s string = "HackerRank "

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	firstInt, err := strconv.ParseUint(scanner.Text(), 10, 64)
	if err != nil {
		return
	}
	firstInt += i
	fmt.Println(firstInt)

	scanner.Scan()
	secondFloat, err := strconv.ParseFloat(scanner.Text(), 64)
	if err != nil {
		return
	}
	secondFloat += d
	fmt.Printf("%0.1f\n", secondFloat)

	scanner.Scan()
	thirdString := scanner.Text()
	fmt.Println(s + thirdString)

	return
}

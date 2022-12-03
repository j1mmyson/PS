package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func isPrime(n int) bool {
	if n == 1 {
		return false
	}

	if n == 2 || n == 3 {
		return true
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	T, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < T; i++ {
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		if isPrime(num) {
			fmt.Println("Prime")
		} else {
			fmt.Println("Not prime")
		}
	}

}

package main

import (
	"fmt"
	"math"
)

func findRoots(a, b, c float64) (float64, float64) {
	n := b / (-2 * a)
	pm := math.Sqrt(b*b-4*(a*c)) / (2 * a)

	return n + pm, n - pm
}

func main() {
	x1, x2 := findRoots(2, 10, 8)
	fmt.Printf("Roots: %f, %f", x1, x2)
}

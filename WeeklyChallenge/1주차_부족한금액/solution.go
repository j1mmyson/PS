package main

import "math"

func getCount(c int) int {
	return c * (c + 1) / 2
}

func solution(price int, money int, count int) int64 {
	return int64(math.Max(0, float64(price*getCount(count)-money)))
}

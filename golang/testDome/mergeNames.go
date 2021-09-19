package main

import "fmt"

func uniqueNames(a, b []string) []string {
	var result []string
	var temp map[string]bool
	temp = make(map[string]bool)
	for _, v := range a {
		_, exists := temp[v]
		if !exists {
			temp[v] = true
		}
	}

	for _, v := range b {
		_, exists := temp[v]
		if !exists {
			temp[v] = true
		}
	}
	for key := range temp {
		result = append(result, key)
	}

	return result
}

func solution1() {
	// should print Ava, Emma, Olivia, Sophia
	fmt.Println(uniqueNames(
		[]string{"Ava", "Emma", "Olivia"},
		[]string{"Olivia", "Sophia", "Emma"}))
}

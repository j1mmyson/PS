package kata

import (
	"reflect"
	"sort"
)

func Comp(array1 []int, array2 []int) bool {

	if array1 == nil || array2 == nil {
		return false
	}

	var temp = []int{}

	for _, v := range array1 {
		temp = append(temp, v*v)
	}

	sort.Ints(temp)
	sort.Ints(array2)

	return reflect.DeepEqual(temp, array2)
}

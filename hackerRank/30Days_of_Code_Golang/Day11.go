package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	var arr [][]int32
	for i := 0; i < 6; i++ {
		arrRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var arrRow []int32
		for _, arrRowItem := range arrRowTemp {
			arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
			checkError(err)
			arrItem := int32(arrItemTemp)
			arrRow = append(arrRow, arrItem)
		}

		if len(arrRow) != 6 {
			panic("Bad input")
		}

		arr = append(arr, arrRow)
	}
	position := [7][2]int{{0, 0}, {0, 1}, {0, 2}, {1, 1}, {2, 0}, {2, 1}, {2, 2}}
	answer := -63
	temp := 0
	for i := 0; i < 4; i++ {
		for j := 0; j < 4; j++ {
			temp = 0
			for _, v := range position {
				temp += int(arr[i+v[0]][j+v[1]])
			}
			if temp > answer {
				answer = temp
			}
		}
	}
	fmt.Println(answer)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func intToBin(n int32) string {
	return strconv.FormatInt(int64(n), 2)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	bNum := intToBin(n)

	answer := 0
	temp := 0
	for _, chr := range bNum {
		if chr == '1' {
			temp += 1
			if temp >= answer {
				answer = temp
			}
		} else {
			temp = 0
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

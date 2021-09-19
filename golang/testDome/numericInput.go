package main

import (
	"fmt"
	"strconv"
)

type UserInput interface {
	Add(rune)
	GetValue() string
}

func (n *NumericInput) Add(r rune) {
	temp := string([]byte(string(r)))
	_, err := strconv.Atoi(temp)
	if err != nil {
		return
	}
	n.input += temp
}

func (n NumericInput) GetValue() string {
	return n.input
}

type NumericInput struct {
	input string
	UserInput
}

func main() {
	var input UserInput = &NumericInput{}
	input.Add('1')
	input.Add('a')
	input.Add('0')
	fmt.Println(input.GetValue())
}

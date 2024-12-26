package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	crates, instructions := loadInput()
	fmt.Println(fmt.Sprint("Final crates on top: ", part1(duplicate(crates), instructions)))
	fmt.Println(fmt.Sprint("Final crates on top with CrateMover 9001: ", part2(crates, instructions)))
}

func loadInput() ([][]byte, [][3]int) {
	bytes, _ := os.ReadFile("input")
	lines := strings.Split(string(bytes), "\n")
	C := (len(lines[0]) + 1) / 4
	crates, instructions := make([][]byte, C), make([][3]int, 0)
	readingInstructions := false
	for _, line := range lines {
		if line == "" {
			continue
		} else if line[:2] == " 1" {
			readingInstructions = true
		} else if readingInstructions {
			var instruction [3]int
			for i, number := range strings.Split(line, " ") {
				if i%2 == 1 {
					instruction[i/2], _ = strconv.Atoi(number)
				}
			}
			instructions = append(instructions, instruction)
		} else {
			for c := 0; c < C; c++ {
				if line[1+c*4] != ' ' {
					crates[c] = append([]byte{line[1+c*4]}, crates[c]...)
				}
			}
		}
	}
	return crates, instructions
}

func part1(crates [][]byte, instructions [][3]int) string {
	for _, instruction := range instructions {
		amount, from, to := instruction[0], instruction[1]-1, instruction[2]-1
		for c := 0; c < amount; c++ {
			crates[to] = append(crates[to], crates[from][len(crates[from])-1])
			crates[from] = crates[from][:len(crates[from])-1]
		}
	}
	res := ""
	for _, crate := range crates {
		res += string(crate[len(crate)-1])
	}
	return res
}

func part2(crates [][]byte, instructions [][3]int) string {
	for _, instruction := range instructions {
		amount, from, to := instruction[0], instruction[1]-1, instruction[2]-1
		crates[to] = append(crates[to], crates[from][len(crates[from])-amount:]...)
		crates[from] = crates[from][:len(crates[from])-amount]
	}
	res := ""
	for _, crate := range crates {
		res += string(crate[len(crate)-1])
	}
	return res
}

func duplicate(input [][]byte) [][]byte {
	res := make([][]byte, len(input))
	for i, row := range input {
		res[i] = make([]byte, len(row))
		copy(res[i], row)
	}
	return res
}

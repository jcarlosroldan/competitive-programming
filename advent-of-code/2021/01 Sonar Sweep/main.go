package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	report := loadReport()
	fmt.Println(fmt.Sprint("Number of increases: ", part1(report)))
	fmt.Println(fmt.Sprint("Number of increases (groups of three): ", part2(report)))
}

func loadReport() []int {
	bytes, _ := os.ReadFile("input")
	resStrings := strings.Split(strings.Trim(string(bytes), "\n"), "\n")
	res := make([]int, len(resStrings))
	for i, s := range resStrings {
		res[i], _ = strconv.Atoi(s)
	}
	return res
}

func part1(report []int) int {
	res := 0
	last := -1
	for _, depth := range report {
		if last != -1 && depth > last {
			res++
		}
		last = depth
	}
	return res
}

func part2(report []int) int {
	compressed := make([]int, len(report) - 2)
	for i := 0; i < len(report) - 2; i++ {
		compressed[i] = report[i] + report[i+1] + report[i+2]
	}
	return part1(compressed)
}
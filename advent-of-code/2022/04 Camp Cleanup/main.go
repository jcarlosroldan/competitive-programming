package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	pairs := loadPairs()
	fmt.Println(fmt.Sprint("Fully contained assigned pairs: ", part1(pairs)))
	fmt.Println(fmt.Sprint("Overlapping pairs: ", part2(pairs)))
}

func loadPairs() [][4]int {
	res := make([][4]int, 0)
	bytes, _ := os.ReadFile("input")
	for _, line := range strings.Split(strings.TrimSpace(string(bytes)), "\n") {
		pair := [4]int{}
		for i, part := range strings.Split(line, ",") {
			for j, num := range strings.Split(part, "-") {
				pair[i*2+j], _ = strconv.Atoi(num)
			}
		}
		res = append(res, pair)
	}
	return res
}

func part1(pairs [][4]int) int {
	res := 0
	for _, assignments := range pairs {
		if assignments[0] >= assignments[2] && assignments[1] <= assignments[3] || assignments[0] <= assignments[2] && assignments[1] >= assignments[3] {
			res++
		}
	}
	return res
}

func part2(pairs [][4]int) int {
	res := 0
	for _, a := range pairs {
		if a[0] <= a[2] && a[1] >= a[2] || a[0] >= a[2] && a[0] <= a[3] {
			res++
		}
	}
	return res
}

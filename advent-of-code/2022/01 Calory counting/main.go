package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	inventory := loadInventory()
	fmt.Println(fmt.Sprint("Top calories: ", part1(inventory)))
	fmt.Println(fmt.Sprint("Sum of top-3 elves: ", part2(inventory)))
}

func loadInventory() [][]int {
	res := make([][]int, 0)
	bytes, _ := os.ReadFile("input")
	for _, chunk := range strings.Split(string(bytes), "\n\n") {
		snacks := make([]int, 0)
		for _, snack := range strings.Split(chunk, "\n") {
			number, _ := strconv.Atoi(snack)
			snacks = append(snacks, number)
		}
		res = append(res, snacks)
	}
	return res
}

func part1(inventory [][]int) int {
	res := 0
	for _, snacks := range inventory {
		total := sum(snacks)
		if total > res {
			res = total
		}
	}
	return res
}

func part2(inventory [][]int) int {
	calories := make([]int, 0)
	for _, snacks := range inventory {
		calories = append(calories, sum(snacks))
	}
	sort.Ints(calories)
	return sum(calories[len(calories)-3:])
}

func sum(elements []int) int {
	res := 0
	for _, element := range elements {
		res += element
	}
	return res
}

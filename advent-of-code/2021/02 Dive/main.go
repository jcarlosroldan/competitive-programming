package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	actions := loadActions()
	fmt.Println(fmt.Sprint("Horizontal position x Depth = ", part1(actions)))
	fmt.Println(fmt.Sprint("Horizontal position x Depth = ", part2(actions)))
}

func loadActions() []string {
	bytes, _ := os.ReadFile("input")
	return strings.Split(strings.TrimSpace(string(bytes)), "\n")
}

func part1(actions []string) int {
	x, y := 0, 0
	for _, line := range actions {
		action := strings.Split(line, " ")
		amount, _ := strconv.Atoi(action[1])
		if action[0] == "forward" {
			x += amount
		} else if action[0] == "up" {
			y -= amount
		} else if action[0] == "down" {
			y += amount
		}
	}
	return x * y
}

func part2(actions []string) int {
	aim, x, y := 0, 0, 0
	for _, line := range actions {
		action := strings.Split(line, " ")
		amount, _ := strconv.Atoi(action[1])
		if action[0] == "down" {
			aim += amount
		} else if action[0] == "up" {
			aim -= amount
		} else {
			x += amount
			y += aim * amount
		}
	}
	return x * y
}
package main

import (
	"fmt"
	"os"
	"strings"
)

var SCORES = map[string]int{
	"rock": 1,
	"paper": 2,
	"scissors": 3,
	"win": 6,
	"draw": 3,
	"lose": 0,
}
var TRANSLATE = map[string]string{
	"A": "rock",
	"B": "paper",
	"C": "scissors",
	"X": "rock",
	"Y": "paper",
	"Z": "scissors",
}
var PRIORITY = [...]string {"rock", "paper", "scissors"}
var TRANSLATE_REAL = map[string]string{
	"X": "lose",
	"Y": "draw",
	"Z": "win",
}

func main() {
	matches := loadMatches()
	fmt.Println(fmt.Sprint("Score following the strategy: ", part1(matches)))
	fmt.Println(fmt.Sprint("Score following the (real) strategy: ", part2(matches)))
}

func loadMatches() []string {
	bytes, _ := os.ReadFile("input")
	return strings.Split(strings.TrimSpace(string(bytes)), "\n")
}

func part1(matches []string) int {
	res := 0
	for _, line := range matches {
		strategy := strings.Split(line, " ")
		opponent := TRANSLATE[strategy[0]]
		me := TRANSLATE[strategy[1]]
		var outcome string
		if opponent == me {
			outcome = "draw"
		} else if opponent == "rock" && me == "paper" || opponent == "paper" && me == "scissors" || opponent == "scissors" && me == "rock" {
			outcome = "win"
		} else {
			outcome = "lose"
		}
		res += points(me, outcome)
	}
	return res
}

func points(me string, outcome string) int {
	return SCORES[me] + SCORES[outcome]
}

func part2(matches []string) int {
	res := 0
	for _, line := range matches {
		strategy := strings.Split(line, " ")
		opponent := TRANSLATE[strategy[0]]
		outcome := TRANSLATE_REAL[strategy[1]]
		var me string
		if outcome == "draw" {
			me = opponent
		} else if outcome == "win" {
			me = PRIORITY[(index(PRIORITY, opponent) + 1) % 3]
		} else {
			me = PRIORITY[(index(PRIORITY, opponent) + 2) % 3]
		}
		res += points(me, outcome)
	}
	return res
}

func index(array [3]string, value string) int {
	for i, element := range array {
		if element == value {
			return i
		}
	}
	return -1
}
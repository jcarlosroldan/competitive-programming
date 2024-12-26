package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	rucksacks := loadRucksacks()
	fmt.Println(fmt.Sprint("Total sum of all priorities is: ", part1(rucksacks)))
	fmt.Println(fmt.Sprint("Total sum of all priorities is: ", part2(rucksacks)))
}

func loadRucksacks() []string {
	bytes, _ := os.ReadFile("input")
	return strings.Split(strings.TrimSpace(string(bytes)), "\n")
}

func part1(rucksacks []string) int {
	res := 0
	for _, rucksack := range rucksacks {
		pocketSize := len(rucksack) / 2
		for left := 0; left < pocketSize; left++ {
			contains := false
			for right := pocketSize; right < len(rucksack); right++ {
				if rucksack[left] == rucksack[right] {
					contains = true
					break
				}
			}
			if contains {
				res += priority(rucksack[left])
				break
			}
		}
	}
	return res
}

func priority(item byte) int {
	if item >= 97 { // lowercase
		return int(item - 96)
	} else { // uppercase
		return int(item - 65 + 27)
	}
}

func part2(rucksacks []string) int {
	res := 0
	for i := 0; i < len(rucksacks); i += 3 {
		res += priority(commonChars(rucksacks[i], commonChars(rucksacks[i+1], rucksacks[i+2]))[0])
	}
	return res
}

func commonChars(a, b string) string {
	res := ""
	for _, char := range a {
		if strings.Contains(b, string(char)) {
			res += string(char)
		}
	}
	return res
}

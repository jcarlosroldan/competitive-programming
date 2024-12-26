package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	signal := loadSignal()
	fmt.Println(signal)
	fmt.Println(fmt.Sprint("The start-of-packet marker is located at position ", part1(signal)))
	fmt.Println(fmt.Sprint("The start-of-message marker is located at position ", part2(signal, 14)))
}

func loadSignal() string {
	bytes, _ := os.ReadFile("input")
	return strings.TrimSpace(string(bytes))
}

func part1(signal string) int {
	for p := 3; p < len(signal); p++ {
		if signal[p] != signal[p-1] && signal[p] != signal[p-2] && signal[p] != signal[p-3] && signal[p-1] != signal[p-2] && signal[p-1] != signal[p-3] && signal[p-2] != signal[p-3] {
			return p + 1
		}
	}
	return -1
}

func part2(signal string, distinctLength int) int {
	for p := 0; p < len(signal)-distinctLength; p++ {
		seen := make(map[string]bool, 26)
		isStart := true
		for c := 0; c < distinctLength; c++ {
			letter := string(signal[p+c])
			if _, exists := seen[letter]; exists {
				isStart = false
				break
			} else {
				seen[letter] = true
			}
		}
		if isStart {
			return p + distinctLength
		}
	}
	return -1
}

// function part2 won't work because

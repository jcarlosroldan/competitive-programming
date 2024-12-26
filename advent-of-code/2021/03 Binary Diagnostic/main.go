package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	report := loadReport()
	fmt.Println("Power consumption: ", part1(report))
}

func loadReport() []string {
	bytes, _ := os.ReadFile("input")
	return strings.Split(strings.TrimSpace(string(bytes)), "\n")
}

func part1(report []string) int {
	mostCommon := make([]int, len(report[0]))
	for _, line := range report {
		for i := 0; i < len(mostCommon); i++ {
			if line[i] == '1' {
				mostCommon[i]++
			} else {
				mostCommon[i]--
			}
		}
	}
	for i := 0; i < len(mostCommon); i++ {
		if mostCommon[i] < 0 {
			mostCommon[i] = 0
		} else if mostCommon[i] > 0 {
			mostCommon[i] = 1
		}
	}
	gamma, epsilon := 0, 0
	for i := 0; i < len(mostCommon); i++ {
		amount := PowInt(2, len(mostCommon) - 1 - i)
		if mostCommon[i] == 1 {
			gamma += amount
		} else {
			epsilon += amount
		}
	}
	return gamma * epsilon
}

func PowInt(x, y int) int {
    return int(math.Pow(float64(x), float64(y)))
}
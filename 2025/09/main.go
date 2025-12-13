package main

import (
	"fmt"
	"os"

	"aoc/utils"
)

func solve(filename string, pt int) int {
	lines, err := utils.ReadLines(filename)
	if err != nil || len(lines) == 0 {
		return -1
	}

	res := 0
	for i, line := range lines {
		_ = i
		_ = line
	}

	return res
}

func main() {
	inputFile := "input.txt"
	if len(os.Args) > 1 {
		inputFile = os.Args[1]
	}

	sol1 := utils.Performance("solve1", func() int { return solve(inputFile, 1) })
	fmt.Printf("\033[1m\033[92m[SOLUTION] i_sol1 = %d\033[0m\n", sol1)

	sol2 := utils.Performance("solve2", func() int { return solve(inputFile, 2) })
	fmt.Printf("\033[1m\033[92m[SOLUTION] i_sol2 = %d\033[0m\n", sol2)
}

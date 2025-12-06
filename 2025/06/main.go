package main

import (
	"fmt"
	"os"
	"strconv"

	"aoc/utils"
)

func solve1(filename string) int {
	lines, err := utils.ReadLines(filename)
	if err != nil || len(lines) == 0 {
		return -1
	}

	var nums [][]int
	var ops []string

	for i, line := range lines {
		if i < len(lines)-1 {
			nums = append(nums, utils.Ints(line))
		} else {
			ops = utils.Anywords(line)
		}
	}

	res := 0
	for c := 0; c < len(nums[0]); c++ {
		ps := 0
		isMul := ops[c] == "*"
		if isMul {
			ps = 1
		}
		for r := 0; r < len(nums); r++ {
			if isMul {
				ps *= nums[r][c]
			} else {
				ps += nums[r][c]
			}
		}
		res += ps
	}

	return res
}

func solve2(filename string) int {
	lines, err := utils.ReadLines(filename)
	if err != nil || len(lines) == 0 {
		return -1
	}

	R := len(lines)
	C := len(lines[0])
	res := 0
	var nums []int

	for c := C - 1; c >= 0; c-- {
		var currn []byte
		for r := 0; r < R; r++ {
			char := lines[r][c]
			if r == R-1 {
				if len(currn) > 0 {
					n, _ := strconv.Atoi(string(currn))
					nums = append(nums, n)
					currn = nil
				}
				if char == '+' {
					sum := 0
					for _, n := range nums {
						sum += n
					}
					res += sum
					nums = nil
				}
				if char == '*' {
					prod := 1
					for _, n := range nums {
						prod *= n
					}
					res += prod
					nums = nil
				}
				continue
			}
			if char != ' ' {
				currn = append(currn, char)
			}
		}
	}

	return res
}

func main() {
	inputFile := "input.txt"
	if len(os.Args) > 1 {
		inputFile = os.Args[1]
	}

	sol1 := utils.Performance("solve1", func() int { return solve1(inputFile) })
	fmt.Printf("\033[1m\033[92m[SOLUTION] i_sol1 = %d\033[0m\n", sol1)

	sol2 := utils.Performance("solve2", func() int { return solve2(inputFile) })
	fmt.Printf("\033[1m\033[92m[SOLUTION] i_sol2 = %d\033[0m\n", sol2)
}

package utils

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"runtime"
	"strconv"
	"time"
)

func Ints(s string) []int {
	re := regexp.MustCompile(`-?\d+`)
	matches := re.FindAllString(s, -1)
	result := make([]int, 0, len(matches))
	for _, m := range matches {
		n, _ := strconv.Atoi(m)
		result = append(result, n)
	}
	return result
}

func Anywords(s string) []string {
	re := regexp.MustCompile(`[^\s]+`)
	return re.FindAllString(s, -1)
}

func Performance(name string, fn func() int) int {
	var memStart runtime.MemStats
	runtime.ReadMemStats(&memStart)
	startTime := time.Now()

	result := fn()

	elapsed := time.Since(startTime)
	var memEnd runtime.MemStats
	runtime.ReadMemStats(&memEnd)
	memUsed := float64(memEnd.Alloc-memStart.Alloc) / 1024 / 1024

	fmt.Printf("\n[[ CPU %.4f sec | Mem %.2f MB ]]\n", elapsed.Seconds(), memUsed)
	return result
}

func ReadLines(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

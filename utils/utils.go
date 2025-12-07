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

func PositiveInts(s string) []int {
	re := regexp.MustCompile(`\d+`)
	matches := re.FindAllString(s, -1)
	result := make([]int, 0, len(matches))
	for _, m := range matches {
		n, _ := strconv.Atoi(m)
		result = append(result, n)
	}
	return result
}

func Floats(s string) []float64 {
	re := regexp.MustCompile(`-?\d+(?:\.\d+)?`)
	matches := re.FindAllString(s, -1)
	result := make([]float64, 0, len(matches))
	for _, m := range matches {
		f, _ := strconv.ParseFloat(m, 64)
		result = append(result, f)
	}
	return result
}

func PositiveFloats(s string) []float64 {
	re := regexp.MustCompile(`\d+(?:\.\d+)?`)
	matches := re.FindAllString(s, -1)
	result := make([]float64, 0, len(matches))
	for _, m := range matches {
		f, _ := strconv.ParseFloat(m, 64)
		result = append(result, f)
	}
	return result
}

func Words(s string) []string {
	re := regexp.MustCompile(`[a-zA-Z]+`)
	return re.FindAllString(s, -1)
}

func AlphabetLower() []string {
	result := make([]string, 26)
	for i := 0; i < 26; i++ {
		result[i] = string(rune('a' + i))
	}
	return result
}

func AlphabetUpper() []string {
	result := make([]string, 26)
	for i := 0; i < 26; i++ {
		result[i] = string(rune('A' + i))
	}
	return result
}

func Alphabet() []string {
	result := make([]string, 52)
	for i := 0; i < 26; i++ {
		result[i] = string(rune('a' + i))
		result[i+26] = string(rune('A' + i))
	}
	return result
}

func IsNumber(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func ManhattanDistance(p, q []int) int {
	distance := 0
	for i := range p {
		diff := p[i] - q[i]
		if diff < 0 {
			diff = -diff
		}
		distance += diff
	}
	return distance
}

func Flatten(nested [][]int) []int {
	var result []int
	for _, inner := range nested {
		result = append(result, inner...)
	}
	return result
}

// UnionFind data structure
type UnionFind struct {
	n       int
	parents []int
	ranks   []int
	NumSets int
}

func NewUnionFind(n int) *UnionFind {
	parents := make([]int, n)
	for i := range parents {
		parents[i] = -1 // -1 means no parent (is root)
	}
	ranks := make([]int, n)
	for i := range ranks {
		ranks[i] = 1
	}
	return &UnionFind{
		n:       n,
		parents: parents,
		ranks:   ranks,
		NumSets: n,
	}
}

func (uf *UnionFind) Find(i int) int {
	if uf.parents[i] == -1 {
		return i
	}
	uf.parents[i] = uf.Find(uf.parents[i])
	return uf.parents[i]
}

func (uf *UnionFind) InSameSet(i, j int) bool {
	return uf.Find(i) == uf.Find(j)
}

func (uf *UnionFind) Merge(i, j int) {
	i = uf.Find(i)
	j = uf.Find(j)

	if i == j {
		return
	}

	iRank := uf.ranks[i]
	jRank := uf.ranks[j]

	if iRank < jRank {
		uf.parents[i] = j
	} else if iRank > jRank {
		uf.parents[j] = i
	} else {
		uf.parents[j] = i
		uf.ranks[i]++
	}
	uf.NumSets--
}

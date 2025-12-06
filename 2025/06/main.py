from utils import *
import operator


#########################################################
#########################################################
@performance
def solve1(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    nums = []
    ops = None
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            nums.append(ints(line))
        else:
            ops = anywords(line)

    for c in range(len(nums[0])):
        op, ps = operator.add, 0
        if ops[c] == "*":
            op, ps = operator.mul, 1
        for r in range(len(nums)):
            ps = op(ps, nums[r][c])
        res += ps

    return res


@performance
def solve2(__file):
    lines = [[x for x in line.rstrip("\n")] for line in open(__file)]
    if len(lines) == 0:
        return -1

    R, C = len(lines), len(lines[0])
    res = 0
    nums = []

    for c in reversed(range(C)):
        currn = []
        for r in range(R):
            char = lines[r][c]
            if r == R - 1:
                if len(currn) > 0:
                    nums.append(int("".join(currn)))
                    currn = []
                if char == "+":
                    res += reduce(operator.add, nums, 0)
                    nums = []
                if char == "*":
                    res += reduce(operator.mul, nums, 1)
                    nums = []
                continue
            if char != " ":
                currn.append(char)
    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve1(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve2(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

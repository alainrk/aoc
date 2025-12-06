from utils import *
import operator


#########################################################
#########################################################
@performance
def solve(__file, pt):
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


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    # i_sol2 = solve(input_file, 2)
    # print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

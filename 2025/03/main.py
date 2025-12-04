from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    bs = []
    for i, line in enumerate(lines):
        bs.append([int(c) for c in line])

    for b in bs:
        max1, max2, maxn = 0, 0, 0

        for i, c in enumerate(b):
            # print(f"{c = }, {max1 = }, {max2 = }, {maxn = }")
            if c * 10 > maxn and i < len(b) - 1:
                maxn, max1, max2 = c * 10, c, 0
                continue
            if max1 * 10 + c > maxn:
                maxn, max1, max2 = max1 * 10 + c, max1, c

        # print(f"{b = }, {max1 = }, {max2 = }, {maxn = }")
        res += max1 * 10 + max2

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

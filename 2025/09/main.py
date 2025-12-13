from utils import *


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    reds = []
    for i, line in enumerate(lines):
        c, r = ints(line)
        reds.append((r, c))

    for i in range(len(reds) - 1):
        for j in range(i + 1, len(reds)):
            res = max(res, area(reds[i], reds[j]))
    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    # i_sol2 = solve(input_file, 2)
    # print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

from utils import *
from functools import reduce
import json

#########################################################
#########################################################
@performance
def solve(__file, pt):
    res = 0

    if pt == 1:
        lines = [line.strip() for line in open(__file)]
        if len(lines) == 0:
            return -1

        res = 0
        for i, line in enumerate(lines):
            res = reduce(lambda x, y: x + y, ints(line))
            break

        return res

    with open(__file) as f:
        data = json.load(f)

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


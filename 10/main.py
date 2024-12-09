from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for i, line in enumerate(lines):
        pass

    # 1st part

    # 2nd part

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    ranges = []
    for n, line in enumerate(lines):
        chunks = line.split(",")
        print(chunks)
        ranges = [list(map(int, x.split("-"))) for x in chunks]
        # Only one line
        break

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            s = str(n)
            l = len(s) // 2
            if s[l:] == s[:l]:
                res += n

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    # i_sol2 = solve(input_file, 2)
    # print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

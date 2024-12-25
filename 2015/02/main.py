from utils import *
from math import prod

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    D = []
    for i, line in enumerate(lines):
        D.append(ints(line))

    # 2*l*w + 2*w*h + 2*h*l
    if pt == 1:
        for d in D:
            l, w, h = d
            s = sorted(d)[:-1]
            res += (2*l*w + 2*w*h + 2*h*l) + (prod(s))
    else:
        for d in D:
            l, w, h = d
            s = sorted(d)[:-1]
            res += 2*s[0]+2*s[1] + l*w*h

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


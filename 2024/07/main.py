import enum
from itertools import product
from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    C = []
    for _, line in enumerate(lines):
        C.append(ints(line))

    if pt == 1:
        for _, c in enumerate(C):
            r, ns = c[0], c[1:]
            ops = [x for x in product(['+', '*'], repeat=len(ns) - 1)]
            for op in ops:
                s = ns[0]
                for i in range(1, len(ns)):
                    cop = op[i - 1]
                    if cop == '+':
                        s += ns[i]
                    else:
                        s *= ns[i]
                if s == r:
                    res += r
                    break

        return res

    if pt == 2:
        for _, c in enumerate(C):
            r, ns = c[0], c[1:]
            ops = [x for x in product(['+', '*', '||'], repeat=len(ns) - 1)]
            for op in ops:
                s = ns[0]
                for i in range(1, len(ns)):
                    cop = op[i - 1]
                    if cop == '+':
                        s += ns[i]
                    elif cop == '*':
                        s *= ns[i]
                    else:
                        s = int(f"{s}{ns[i]}")
                if s == r:
                    res += r
                    break

        return res

    
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    # i_sol = solve(input_file, 1)
    i_sol = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


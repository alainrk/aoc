from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    M = 1000

    res = 0
    G = [[0 for _ in range(M)] for _ in range(M)]
    for i, line in enumerate(lines):
        on, off, toggle = False, False, False
        x0, y0, x1, y1 = ints(line)

        if "on" in line:
            on = True
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    G[x][y] = 1
        elif "off" in line:
            off = True
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    G[x][y] = 0
        elif "toggle" in line:
            toggle = True
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    G[x][y] = 1 - G[x][y]
        else:
            assert False

    for i, r in enumerate(G):
        for _, l in enumerate(r):
            res += 1 if l else 0
        print()

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")
""

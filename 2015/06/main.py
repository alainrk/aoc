from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    M = 1000

    res = 0
    G = [[0 for _ in range(M)] for _ in range(M)]
    for i, line in enumerate(lines):
        x0, y0, x1, y1 = ints(line)

        if "on" in line:
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    if pt == 1:
                        G[x][y] = 1
                    else:
                        G[x][y] += 1
        elif "off" in line:
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    if pt == 1:
                        G[x][y] = 0
                    else:
                        G[x][y] = max(0, G[x][y] - 1)
        elif "toggle" in line:
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    if pt == 1:
                        G[x][y] = 1 - G[x][y]
                    else:
                        G[x][y] += 2
        else:
            assert False

    for i, r in enumerate(G):
        for _, l in enumerate(r):
            if pt == 1:
                res += 1 if l else 0
            else:
                res += l

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

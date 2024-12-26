from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    dirs = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    res = 1

    pos = (0, 0)
    rpos = (0, 0)

    V = set([pos])

    for i, line in enumerate(lines):
        for j, d in enumerate(line):
            if pt == 1 or j % 2 == 0:
                pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
                if pos not in V:
                    res += 1
                V.add(pos)
            elif j % 2 == 1:
                rpos = (rpos[0] + dirs[d][0], rpos[1] + dirs[d][1])
                if rpos not in V:
                    res += 1
                V.add(rpos)
            else:
                assert False

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


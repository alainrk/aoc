from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = set()
    res2 = set()
    G = []
    for i, line in enumerate(lines):
        l = list(line)
        G.append(l)

    R,C = len(G), len(G[0])
    # for each freq antenna, where they are
    A = defaultdict(list)
    for i in range(R):
        for j in range(C):
            if G[i][j] != ".":
                A[G[i][j]].append((i,j))

    # for each possible pos in the grid
    for r in range(R):
        for c in range(C):
            # for each pair of same antennas
            for a, pos in A.items():
                for x1, y1 in pos:
                    for x2, y2 in pos:
                        if (x1, y1) == (x2, y2):
                            continue

                        d1 = abs(x1 - r) + abs(y1 - c)
                        d2 = abs(x2 - r) + abs(y2 - c)

                        dx1, dy1 = r - x1, c - y1
                        dx2, dy2 = r - x2, c - y2

                        if (d1 == 2 * d2 or d1 * 2 == d2) and 0 <= r < R and 0 <= c < C and (dx1 * dy2 == dy1 * dx2):
                            res.add((r, c))
                        if 0 <= r < R and 0 <= c < C and (dx1 * dy2 == dy1 * dx2):
                            res2.add((r, c))


    return len(res), len(res2)
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


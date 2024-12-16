from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    G = []
    S, E = [-1, -1], [-1, -1]
    for i, line in enumerate(lines):
        g = []
        for j, c in enumerate(line):
            if c == "S":
                S = (i, j)
            elif c == "E":
                E = (i, j)
            g.append(c)
        G.append(g)

    R,C = len(G), len(G[0])

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    # Priority queue: (cost, (row, col, dir))
    Q = [(0, (S[0], S[1], 0))]
    V = defaultdict(lambda: float('inf'))
    V[(S[0], S[1], 0)] = 0

    while Q:
        cost, (r, c, d) = heappop(Q)

        if (r, c) == E:
            return cost

        # all possible moves
        for new_d in range(4):
            # rotation cost
            rotation_cost = min((new_d - d) % 4, (d - new_d) % 4) * 1000

            # move to new dir
            nr, nc = r + dirs[new_d][0], c + dirs[new_d][1]

            if (0 <= nr < R and 0 <= nc < C and
                G[nr][nc] != '#' and
                cost + rotation_cost + 1 < V[(nr, nc, new_d)]):

                new_cost = cost + rotation_cost + 1
                V[(nr, nc, new_d)] = new_cost
                heappush(Q, (new_cost, (nr, nc, new_d)))
    return -1

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


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

    # visited so far and init with S
    mincost = defaultdict(lambda: float('inf'))
    mincost[(S[0], S[1], 0)] = 0
    backtrack = defaultdict(set)
    res = float('inf')
    ends = set()

    while Q:
        cost, (r, c, d) = heappop(Q)
        if cost > mincost[(r, c, d)]:
            continue

        if (r, c) == E:
            if cost > res:
                if pt==1:
                    return res
                break
            res = cost
            ends.add((r, c, d))

        # all possible moves
        for newdir in range(4):
            # rotation cost (gets the least number of rotations to go in that direction)
            rotation_cost = min((newdir - d) % 4, (d - newdir) % 4) * 1000

            # move to new dir
            nr, nc = r + dirs[newdir][0], c + dirs[newdir][1]

            # no outside, no wall, and no if we already found a shorter path (visited cost is less)
            if not (0 <= nr < R and 0 <= nc < C): continue
            if G[nr][nc] == '#': continue
            res = mincost[(nr, nc, newdir)]
            new_cost = cost + rotation_cost + 1
            if new_cost > res:
                continue
            if new_cost < res:
                backtrack[(nr, nc, newdir)] = set()
                mincost[(nr, nc, newdir)] = new_cost
            backtrack[(nr, nc, newdir)].add((r, c, d))
            heappush(Q, (new_cost, (nr, nc, newdir)))

    # compute back the result
    states = deque(ends)
    seen = set(ends)

    while states:
        k = states.popleft()
        for last in backtrack[k]:
            if last in seen: continue
            seen.add(last)
            states.append(last)


    return(len({(r, c) for r, c, _ in seen}))

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


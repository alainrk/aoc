from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0

    R = 71
    S = (0, 0)
    E = (70, 70)
    G = [[0 for _ in range(R)] for _ in range(R)]
    for i, line in enumerate(lines):
        y, x = ints(line)
        G[x][y] = 1
        if i >= 1023:
            q = [(0, S)]
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            V = set()
            dists = defaultdict(lambda: float("inf"))
            dists[S] = 0

            while q:
                dist, (cx, cy) = heappop(q)
                if (cx, cy) in V:
                    continue

                V.add((cx, cy))

                for d in dirs:
                    nx, ny = cx + d[0], cy + d[1]
                    if nx < 0 or nx >= R or ny < 0 or ny >= R:
                        continue
                    if G[nx][ny] == 1:
                        continue

                    ndist = dist + 1
                    if ndist < dists[(nx, ny)]:
                        dists[(nx, ny)] = ndist
                        heappush(q, (ndist, (nx, ny)))
            if pt == 1:
                return dists[E]
            if dists[E] > 10000:
                return (y, x)

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


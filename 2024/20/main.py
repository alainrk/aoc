from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    S, E = (-1, -1), (-1, -1)
    F = set() # free spaces

    def shortest_paths(start, F):
        Q = [(0, start)]
        dists = defaultdict(lambda: float("inf"))
        dists[start] = 0

        while Q:
            dist, (cx, cy) = heappop(Q)
            if dists[(cx, cy)] < dist:
                continue

            for d in dirs:
                nx, ny = cx + d[0], cy + d[1]
                if (nx, ny) not in F:
                    continue

                if dists[(nx, ny)] > dist + 1:
                    dists[(nx, ny)] = dist + 1
                    heappush(Q, (dist + 1, (nx, ny)))

        return dists

    def get_savings(dists, j, F):
        res = 0
        for f in F:
            for dx, dy in product(range(-j, j+1), repeat=2):
                if dx == dy == 0 or abs(dx) + abs(dy) > j:
                    continue
                # Only keep jumps of length 1 or 2
                nf = (f[0]+dx, f[1]+dy)
                if nf not in F:
                    continue
                without = abs(f[0]-nf[0]) + abs(f[1]-nf[1])
                with_walls = dists[nf] - dists[f]

                if (with_walls - without) >= 100:
                    res += 1
        return res


    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in "ES.":
                F.add((i, j))
            if c == "S":
                S = (i, j)
            if c == "E":
                E = (i, j)

    dists = shortest_paths(E, F)
    if pt == 1:
        res = get_savings(dists, 2, F)
    else:
        res = get_savings(dists, 20, F)

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


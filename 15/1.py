from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    D = { "^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1) }
    G = []
    M = []
    rx, ry = -1, -1
    phase = 0
    for i, line in enumerate(lines):
        if line == "":
            phase = 1
            continue
        if phase == 0:
            G.append(list(line))
            r = line.find("@")
            if r >= 0:
                rx, ry = len(G) - 1, r
        else:
            M.extend(map(lambda m: D[m], list(line)))

    R, C = len(G), len(G[0])

    # Given current pos and direction, find next spot, returns None if no free spot (i.e. wall at some point)
    def next_free_spot_in_dir(x, y, dx, dy):
        while True:
            x, y = x + dx, y + dy
            if G[x][y] == "#": return None
            if G[x][y] == "O": continue
            if G[x][y] == ".":
                return (x, y)

    for (mx, my) in M:
        nx, ny = mx + rx, my + ry
        # Direct wall
        if G[nx][ny] == "#": continue
        # Free space, move and go on
        if G[nx][ny] == ".":
            G[rx][ry] = "."
            G[nx][ny] = "@"
            rx, ry = nx, ny
            continue
        # Box hit
        if G[nx][ny] == "O":
            freespot = next_free_spot_in_dir(nx, ny, mx, my)
            if freespot is None:
                continue
            # "Shift" everything by:
            # Move a box in the free spot
            # Move robot to the next cell
            # Free current cell up from the robot
            fx, fy = freespot
            G[fx][fy] = "O"
            G[nx][ny] = "@"
            G[rx][ry] = "."
            rx, ry = nx, ny

    for r in range(R):
        for c in range(C):
            if G[r][c] == "O":
                res += (100 * r) + c

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


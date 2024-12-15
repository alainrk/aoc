from utils import *
import time

#########################################################
#########################################################
def solve(__file):
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
            g = []
            for c in list(line):
                if c == "#":
                    g.append("#")
                    g.append("#")
                if c == "@":
                    g.append("@")
                    g.append(".")
                if c == ".":
                    g.append(".")
                    g.append(".")
                if c == "O":
                    g.append("[")
                    g.append("]")
            G.append(g)
        else:
            M.extend(map(lambda m: D[m], list(line)))

    R, C = len(G), len(G[0])
    b = False
    for r in range(R):
        for c in range(C):
            if G[r][c] == "@":
                rx, ry = r, c
                G[r][c] = "."
                b = True
                break
        if b:
            break

    def printg():
        time.sleep(0.001)
        # clear screen
        print("\x1b[2J")
        for r in range(R):
            if r == rx:
                g = G[r].copy()
                g[ry] = "@"
                print("".join(g))
            else:
                print("".join(G[r]))

    for mx, my in M:
        nx, ny = mx + rx, my + ry
        # Direct wall
        if G[nx][ny] == "#": 
            printg()
            continue
        # Free space, move and go on
        elif G[nx][ny] == ".":
            printg()
            rx, ry = nx, ny
            continue
        # Box hit
        elif G[nx][ny] in ["[", "]"]:
            q = deque([(rx, ry)])
            s = set()
            go = True
            while q:
                x, y = q.popleft()
                if (x, y) in s:
                    continue
                s.add((x, y))
                dx, dy = x + mx, y + my
                # if a wall is met while moving everything, just stop this move entirely
                if G[dx][dy] == "#":
                    go = False
                    break
                # if meet part of a box, put it in the queue, to be moved along with the rest
                if G[dx][dy]=='[':
                    q.append((dx,dy))
                    # also move its other side
                    q.append((dx,dy+1))
                if G[dx][dy]==']':
                    q.append((dx,dy))
                    # also move its other side
                    q.append((dx,dy-1))
            if not go:
                printg()
                continue
            # empty the queue, moving everything from last in the grid to first
            while len(s):
                # for each box-side to move
                for x, y in sorted(s):
                    newx, newy = x + mx, y + my
                    if (newx, newy) not in s:
                        assert G[newx][newy] == '.'
                        G[newx][newy] = G[x][y]
                        G[x][y] = "."
                        s.remove((x, y))
                        printg()
            rx += mx
            ry += my
            printg()

    for r in range(R):
        for c in range(C):
            if G[r][c] == "[":
                res += (100 * r) + c

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol2 = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


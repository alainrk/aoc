from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    grid = []

    for i, line in enumerate(lines):
        grid.append([x for x in line])

    R, C = len(grid), len(grid[0])
    newgrid = deepcopy(grid)

    while True:
        removed = False
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == ".":
                    continue

                neighbours = 0
                breakloop = False
                for d in dirs:
                    x, y = r + d[0], c + d[1]
                    if x < 0 or x >= R or y < 0 or y >= C:
                        continue
                    if grid[x][y] == "@":
                        neighbours += 1
                    if neighbours > 3:
                        breakloop = True
                        break

                if breakloop:
                    continue
                newgrid[r][c] = "."
                removed = True
                res += 1
        if pt == 1:
            break
        grid = deepcopy(newgrid)
        if not removed:
            break

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

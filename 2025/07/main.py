from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    grid = []
    for i, line in enumerate(lines):
        grid.append([x for x in line])

    R, C = len(lines), len(lines[0])
    sx, sy = 0, lines[0].index("S")

    beamys = set([sy])
    all = []
    timelines = defaultdict(int)
    timelines[sy] = 1

    for r in range(1, R):
        new_beamys = deepcopy(beamys)
        newtimelines = defaultdict(int)

        for c, char in enumerate(grid[r]):
            if char == "^" and c in beamys:
                if pt == 1:
                    res += 1
                new_beamys.discard(c)
                left, right = c - 1, c + 1
                if left >= 0:
                    newtimelines[left] += timelines[c]
                    new_beamys.add(left)
                if right < C:
                    newtimelines[right] += timelines[c]
                    new_beamys.add(right)
            else:
                newtimelines[c] += timelines[c]
                if c in beamys:
                    new_beamys.add(c)

        beamys = new_beamys
        timelines = newtimelines

    if pt == 2:
        for t in timelines:
            res += timelines[t]

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

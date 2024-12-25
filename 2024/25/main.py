from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    isKey = None
    count = 0
    keys, locks = [], []

    for i, line in enumerate(lines):
        if line == "":
            isKey = None
            count = 0
            continue
        count += 1
        if isKey is None:
            if line.startswith("#"):
                isKey = False
                locks.append([0, 0, 0, 0, 0])
                continue
            else:
                isKey = True
                keys.append([0, 0, 0, 0, 0])
        if isKey and count < 7:
            for j, c in enumerate(line):
                if c == "#":
                    keys[len(keys) - 1][j] += 1
        if not isKey:
            for j, c in enumerate(line):
                if c == "#":
                    locks[len(locks) - 1][j] += 1

    for k in keys:
        for l in locks:
            if all(map(lambda x: x[0] + x[1] < 6, zip(k, l))):
                res += 1

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")


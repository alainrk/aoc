from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    ranges = []
    ingredients = []
    scanpt = 0
    for i, line in enumerate(lines):
        if line == "":
            scanpt = 1
            continue
        if scanpt == 0:
            ranges.append(list(map(int, line.split("-"))))
            continue
        ingredients.append(int(line))

    ranges.sort()

    for i in ingredients:
        # print(i)
        for r in ranges:
            # print("   ", r)
            if r[0] <= i <= r[1]:
                # print(f"{i = }, {r[0] = }, {r[1] = }")
                res += 1
                break
            if i < r[1]:
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

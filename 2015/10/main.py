from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = []
    for _, line in enumerate(lines):
        res = list(line)
        break

    for _ in range(40 if pt == 1 else 50):
        input = res.copy()
        res = []
        prev = input[0]
        count = 0
        for _, c in enumerate(input):
            if c == prev:
                count += 1
            elif c != prev:
                res.extend(list(str(count)))
                res.append(prev)
                count = 1
            else:
                assert False
            prev = c
        # last digit
        if input[:-1] == prev:
            res.extend(list(str(count)))
            res.append(prev)
        else:
            res.extend(["1", prev])

    return len(res)

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


from utils import *

#########################################################
#########################################################
#########################################################
def isSafe(R):
    isInc = None

    for i in range(1, len(R)):
        d = R[i] - R[i-1]

        if isInc is None:
            isInc = d > 0
        if isInc is True and d <= 0:
            return [False, i]
        if isInc is False and d >= 0:
            return [False, i]

        diff = abs(d)

        if diff > 3 or diff == 0:
            return [False, i]

    return [True, -1]

def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for _, line in enumerate(lines):
        R = [x for x in map(int, line.split())]
        safe, _ = isSafe(R)

        if safe:
            res += 1

    return res


def solve2(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for _, line in enumerate(lines):
        R = [x for x in map(int, line.split())]
        safe, _ = isSafe(R)
        if safe:
            res += 1
            continue

        for j in range(len(R)):
            RR = R[:j] + R[j+1:]
            safe, _ = isSafe(RR)
            if safe:
                res += 1
                break
    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    i_sol = solve2(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for _, line in enumerate(lines):
        p = r'mul\((\d{1,3}),(\d{1,3})\)'
        M = re.finditer(p, line)
        for m in M:
            x, y = int(m.group(1)), int(m.group(2))
            res += x * y

    return res

def solve2(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    on = True

    for _, line in enumerate(lines):
        p = r'(?:mul\((\d{1,3}),(\d{1,3})\)|(?:do|don\'t)\(\))'
        M = re.finditer(p, line)

        for m in M:
            op = m.group(0)
            x, y = 0, 0
            print(op)
            if op.startswith("mul"):
                x, y = int(m.group(1)), int(m.group(2))
                if on:
                    res += x * y
                    print(x, y, res)
            if op.startswith("don"):
                on = False
            if op.startswith("do("):
                on = True

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    i_sol = solve2(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


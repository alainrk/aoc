from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    gatesPhase = 0
    print("graph TD")
    for i, line in enumerate(lines):
        if line == "":
            gatesPhase +=1
            continue

        if not gatesPhase:
            g, v = line.split(": ")
            print(f"    {g}[{g}]")
        else:
            expr, w = line.split(' -> ')
            parts = expr.split()
            if len(parts) == 3:  # Binary operation (AND/XOR)
                x, op, y = parts
            else:
                assert False
            print(f"    {x} -->|{op}| {w}")
            print(f"    {y} -->|{op}| {w}")


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


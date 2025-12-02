from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    dial = 50

    for line in lines:
        sign, amount = -1 if line[0] == "L" else 1, int(line[1:])

        prev = dial
        dial += sign * amount

        if pt == 1:
            if dial % 100 == 0:
                res += 1
        else:
            # Right
            if sign == 1:
                # Formula: floor(end/100) - floor(start/100)
                # Example: Start 99, Move 2 -> End 101. 101//100 (1) - 99//100 (0) = 1 click.
                res += (dial // 100) - (prev // 100)

            # Left
            else:
                # Formula: is shifted by -1 because leaving 0 (going 0 -> -1) does NOT count.
                # Only arriving at 0 (1 -> 0) counts.
                res += ((prev - 1) // 100) - ((dial - 1) // 100)

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

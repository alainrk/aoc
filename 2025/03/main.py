from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    K = 2 if pt == 1 else 12

    res = 0
    bs = []
    for i, line in enumerate(lines):
        bs.append([int(c) for c in line])

    for b in bs:
        stack = [b[0]]
        drops = len(b) - K

        for c in b[1:]:
            while len(stack) and drops > 0 and c > stack[-1]:
                stack.pop()
                drops -= 1
            if len(stack) < K:
                stack.append(c)
            else:
                drops -= 1

        res += int("".join(map(str, stack)))

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

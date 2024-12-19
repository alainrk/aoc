from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    phase = 1
    A = set() # available
    D = [] # designs
    for i, line in enumerate(lines):
        if line == "":
            phase += 1
            continue
        if phase == 1:
            A = set(words(line))
        elif phase == 2:
            D.append(line)

    def possible(d, M=None):
        if not M:
            M = defaultdict(int)
        if not d:
            return 1
        if M[d] > 0:
            return M[d]
        tot = 0
        for a in A:
            if d.startswith(a):
                tot += possible(d[len(a):], M)

        M[d] = tot
        return tot

    tot = 0
    for d in D:
        p = possible(d)
        tot += p
        if p:
            res += 1

    return res, tot
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")


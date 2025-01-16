from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = float("-inf")

    P = {}
    for i, line in enumerate(lines):
        r = parse("{p1} would {action} {amount} happiness units by sitting next to {p2}.", line)
        if r["p1"] not in P:
            P[r["p1"]] = {}
        P[r["p1"]][r["p2"]] = int(r["amount"]) * (1 if r["action"] == "gain" else -1)


    def happiness(perm):
        h = 0
        l = [perm[-1]] + list(perm) + [perm[0]]
        for i in range(1, len(l) - 1):
            prev, curr, next = l[i-1], l[i], l[i+1]
            h += P[curr][prev]
            h += P[curr][next]
        return h

    for p in permutations(P.keys()):
        h = happiness(p)
        if h > res:
            res = h

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


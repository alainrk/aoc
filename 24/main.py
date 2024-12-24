from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    if pt ==2 : return

    res = 0

    W = {}

    ops = deque()
    gatesPhase = 0
    for i, line in enumerate(lines):
        if line == "":
            gatesPhase +=1
            continue

        if not gatesPhase:
            g, v = line.split(": ")
            W[g] = int(v)
        else:
            expr, w = line.split(' -> ')
            parts = expr.split()
            if len(parts) == 3:  # Binary operation (AND/XOR)
                x, op, y = parts
                ops.append((x, op, y, w))
            else:
                assert False

    while len(ops):
        curr = ops.popleft()
        x, op, y, r = curr
        if x not in W or y not in W:
            ops.append(curr)
            continue

        t = None
        if op == "AND":
            t = W[x] & W[y]
        if op == "OR":
            t = W[x] | W[y]
        if op == "XOR":
            t = W[x] ^ W[y]

        assert t is not None
        print(W[x], op, W[y], "=", t)

        W[r] = t


    for w in sorted(W.keys()):
        print(w, W[w])

    keys = sorted([k for k in W.keys() if k.startswith('z')], reverse=True)
    print(keys)
    d = "".join(list(map(lambda x: str(x), list(W[k] for k in keys))))
    print(d)
    res = int(d, 2)

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


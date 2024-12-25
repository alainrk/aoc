from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    swaps = {
        "z07": "nqk",
        "z24": "fpq",
        "z32": "srn",
        "pcp": "fgt",
    }

    SWAPS = {}
    for k, v in swaps.items():
        SWAPS[k] = v
        SWAPS[v] = k

    W = {}

    # graph (Childs)
    C = defaultdict(set)
    # deps (Parents)
    P = defaultdict(set)

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

                if w in SWAPS:
                    w = SWAPS[w]

                ops.append((x, op, y, w))
                C[x].add(w)
                C[y].add(w)
                P[w].add(x)
                P[w].add(y)
            else:
                assert False

    # Chain of dependencies
    # start with "roots" (empty parents)
    empties = [w for w in W if len(P[w]) == 0]
    sortedWires = []
    e = set(empties)

    depths = defaultdict(int)

    # Topsort
    PP = deepcopy(P)
    while len(empties):
        w = empties.pop()
        sortedWires.append(w)
        # for each child of this current node (being at this stage a root - no parents)
        for x in C[w]:
            depths[x] += 1
            # remove the current node as a parent of its child
            PP[x].remove(w)
            # if this child has no more parents, add it to the roots to be processed
            if len(PP[x]) == 0:
                empties.append(x)

    # Run as it is
    count = 0
    while len(ops):
        count += 1
        if count > 10000:
            break
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

        W[r] = t

    xs = sorted([k for k in W.keys() if k.startswith('x')], reverse=True)
    ys = sorted([k for k in W.keys() if k.startswith('y')], reverse=True)
    zs = sorted([k for k in W.keys() if k.startswith('z')], reverse=True)

    X = "".join(list(map(lambda x: str(x), list(W[k] for k in xs))))
    Y = "".join(list(map(lambda y: str(y), list(W[k] for k in ys))))
    Z = "".join(list(map(lambda z: str(z), list(W[k] for k in zs))))

    # print(X, Y, Z)
    X, Y, Z = int(X, 2), int(Y, 2), int(Z, 2)
    # print(X + Y, Z, X + Y == Z)
    actualZ = X+Y

    def xor(a, b):
        a = map(lambda x: int(x), list(str(bin(a))[2:]))
        b = map(lambda x: int(x), list(str(bin(b))[2:]))
        return "".join(list(map(lambda x, y: str(x ^ y), a, b)))

    print(str(bin(Z))[2:])
    print(str(bin(actualZ))[2:])
    Zxor = xor(Z, actualZ)
    print(Zxor)
    print(zs)
    print(f"Differences {Zxor.count('1')}")


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol2 = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    W = {}
    for i, line in enumerate(lines):
        in1, in2, out = None, None, None

        if "AND" in line:
            in1, op, in2, _, out = line.split(" ")
        elif "OR" in line:
            in1, op, in2, _, out = line.split(" ")
        elif "RSHIFT" in line:
            in1, op, in2, _, out = line.split(" ")
        elif "LSHIFT" in line:
            in1, op, in2, _, out = line.split(" ")
        elif "NOT" in line:
            op, in1, _, out = line.split(" ")
        else:
            op = "ASSIGN"
            in1, _, out = line.split(" ")

        W[out] = [None, op, in1, in2]

    def getval(w):
        if w.isdigit():
            return int(w)
        return resolve(w)

    def resolve(w):
        wire = W[w]
        if wire and wire[0] is not None:
            return wire[0]

        _, op, x, y = wire

        t = None
        if op == "NOT":
            t = ~getval(x) & 0xFFFF
        if op == "AND":
            t = (getval(x) & getval(y))
        if op == "OR":
            t = (getval(x) | getval(y))
        if op == "RSHIFT":
            t = (getval(x) >> getval(y)) & 0xFFFF
        if op == "LSHIFT":
            t = (getval(x) << getval(y)) & 0xFFFF
        if op == "ASSIGN":
            t = getval(x)

        if w not in W:
            assert False
            W[w] = (None, None, None, None)
        W[w][0] = t

        return t

    res = resolve("a")
    if pt == 1:
        return res

    for w in W:
        W[w][0] = None
    W["b"][0] = res
    res = resolve("a")

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


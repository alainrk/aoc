from copy import copy
from utils import *
from functools import cache

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    codes = [line.rstrip("\n") for line in open(__file, "r")]

    doorpad = ["789", "456", "123", "X0A"]
    dronepad = ["X^A", "<v>"]

    def pos(key, keypad):
        for r, row in enumerate(keypad):
            for c, char in enumerate(row):
                if char == key:
                    return r, c
        assert False


    def get_shortests_paths(x, y, keypad):
        r1, c1 = pos(x, keypad)
        r2, c2 = pos(y, keypad)
        r_gap, c_gap = pos("X", keypad)
        dr, dc = r2 - r1, c2 - c1

        updown = "v" * abs(dr) if dr >= 0 else "^" * abs(dr)
        leftright = ">" * abs(dc) if dc >= 0 else "<" * abs(dc)

        if dr == dc == 0:
            return [""]
        elif dr == 0:
            return [leftright]
        elif dc == 0:
            return [updown]
        elif (r1, c2) == (r_gap, c_gap):
            return [updown + leftright]
        elif (r2, c1) == (r_gap, c_gap):
            return [leftright + updown]
        else:
            return [updown + leftright, leftright + updown]


    def get_seqs_shortests_paths(seq, keypad):
        res = []
        for key1, key2 in zip("A" + seq, seq):
            res += [[sp + "A" for sp in get_shortests_paths(key1, key2, keypad)]]
        return res


    @cache
    def subsolve(seq, depth):
        if depth == 1:
            return len(seq)

        if any(c in seq for c in "012345679"):
            keypad = doorpad
        else:
            keypad = dronepad

        res = 0
        for shortest_paths in get_seqs_shortests_paths(seq, keypad):
            res += min(subsolve(sp, depth - 1) for sp in shortest_paths)
        return res


    res = 0
    if pt == 1:
        for code in codes:
            res += subsolve(code, 1 + 2 + 1) * int(code[:3])
    else: 
        for code in codes:
            res += subsolve(code, 1 + 25 + 1) * int(code[:3])
    return res

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


'''
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
'''

from utils import *

#########################################################
#########################################################
G = []

# c == currently searched char at i, j
def xmas(i, j, c, dir, N, F):
    if i < 0 or i >= len(G):
        return 0

    if j < 0 or j >= len(G[0]):
        return 0

    if G[i][j] != c:
        return 0

    # xmaS found
    if G[i][j] == F:
        return 1

    if dir == "u":
        return xmas(i - 1, j, N[c], "u", N, F)
    if dir == "d":
        return xmas(i + 1, j, N[c], "d", N, F)
    if dir == "l":
        return xmas(i, j - 1, N[c], "l", N, F)
    if dir == "r":
        return xmas(i, j + 1, N[c], "r", N, F)
    if dir == "ul":
        return xmas(i - 1, j - 1, N[c], "ul", N, F)
    if dir == "ur":
        return xmas(i - 1, j + 1, N[c], "ur", N, F)
    if dir == "dl":
        return xmas(i + 1, j - 1, N[c], "dl", N, F)
    if dir == "dr":
        return xmas(i + 1, j + 1, N[c], "dr", N, F)

    return 0


def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for i, line in enumerate(lines):
        G.append(list(line))

    R, C = len(G), len(G[0])
    N = { "X": "M", "M": "A", "A": "S" }
    F = "S"

    for i in range(R):
        for j in range(C):
            if G[i][j] != "X":
                continue
            res += xmas(i, j, "X", "u", N, F)
            res += xmas(i, j, "X", "d", N, F)
            res += xmas(i, j, "X", "l", N, F)
            res += xmas(i, j, "X", "r", N, F)
            res += xmas(i, j, "X", "ul", N, F)
            res += xmas(i, j, "X", "ur", N, F)
            res += xmas(i, j, "X", "dl", N, F)
            res += xmas(i, j, "X", "dr", N, F)

    return res

def solve2(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for i, line in enumerate(lines):
        G.append(list(line))

    R, C = len(G), len(G[0])

    for i in range(R):
        for j in range(C):
            if G[i][j] != "A":
                continue
            M = 0
            S = 0
            
            Mul = xmas(i, j, "A", "ul", {"A": "M"}, "M")
            Mur = xmas(i, j, "A", "ur", {"A": "M"}, "M")
            Mdl = xmas(i, j, "A", "dl", {"A": "M"}, "M")
            Mdr = xmas(i, j, "A", "dr", {"A": "M"}, "M")
            M = Mul + Mur + Mdl + Mdr

            Sul = xmas(i, j, "A", "ul", {"A": "S"}, "S")
            Sur = xmas(i, j, "A", "ur", {"A": "S"}, "S")
            Sdl = xmas(i, j, "A", "dl", {"A": "S"}, "S")
            Sdr = xmas(i, j, "A", "dr", {"A": "S"}, "S")
            S = Sul + Sur + Sdl + Sdr

            if M + S != 4:
                continue

            if Mul == Mdr == 1:
                continue

            if Sul == Sdr == 1:
                continue

            if Sur == Sdl == 1:
                continue

            if Mdl == Mur == 1:
                continue

            res += 1

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    i_sol = solve2(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


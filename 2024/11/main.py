from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    S = lines[0].split(" ")
    C = Counter(S)

    for _ in range(25 if pt==1 else 75):
        newc = Counter()
        for s, c in C.items():
            if s == "0":
               newc["1"] += c
            elif len(s)%2 == 0:
                a, b = s[:len(s)//2], str(int(s[len(s)//2:]))
                newc[a] += c
                newc[b] += c
            else:
                newc[str(int(s)*2024)] += c
        C = newc

    return sum(C.values())
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


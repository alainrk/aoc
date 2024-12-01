from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    LL, RR = [], []
    S = defaultdict(int)
    for i, line in enumerate(lines):
        L, R = line.split()
        L = int(L)
        R = int(R)
        S[R] += 1
        LL.append(L)
        RR.append(R)
    LL = sorted(LL)
    RR = sorted(RR)

    # 1st part
    res = 0
    for i in range(len(LL)):
        res += abs(LL[i] - RR[i])

    # 2nd part
    res2 = 0
    for i in range(len(LL)):
        res2 += ( S[LL[i]] * LL[i] )

    return res, res2
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    i_sol = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


from utils import *
from functools import cache

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    N = []
    for i, line in enumerate(lines):
        N.append(ints(line)[0])

    def mixprune(value, secret):
        secret ^= value
        secret %= 16777216
        return secret

    def calc(v):
        v = mixprune(v * 64, v)
        v = mixprune(v // 32, v)
        v = mixprune(v * 2048, v)
        return v

    C = 2000
    # C = 20

    if pt == 1:
        for n in N:
            v = n
            for _ in range(C):
                v = calc(v)
            res += v
        return res

    M = defaultdict(int)
    for n in N:
        v = n
        price, prevprice, diff = v % 10, v % 10, 0
        seq = deque([0])
        V = set()

        for _ in range(C):
            v = calc(v)
            prevprice, price = price, v % 10
            diff = price - prevprice
            if len(seq) > 3:
                seq.popleft()
            seq.append(diff)

            k = tuple(seq)
            if len(k) < 4 or k in V:
                continue
            V.add(k)
            M[k] += price
            # print(f"{n}: {v} {diff}")

    maxv, maxs = 0, None
    for k, v in M.items():
        if v > maxv:
            maxv, maxs = v, k

    return maxv, maxs
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

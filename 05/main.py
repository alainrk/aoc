from utils import *
from collections import defaultdict, deque

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res1 = 0
    res2 = 0
    S = 0
    P = []
    B = defaultdict(set)
    A = defaultdict(set)
    for i, line in enumerate(lines):
        if line.strip() == "":
            S += 1
            continue
        if S == 0:
            a,b = ints(line)
            B[b].add(a)
            A[a].add(b)
            continue
        l = list(map(int, line.split(",")))
        P.append(l)

    def isCorrect(l):
        for i in range(len(l)-1):
            for j in range(i+1, len(l)):
                if not l[j] in A[l[i]]:
                    return False
        return True

    for l in P:
        if isCorrect(l):
            res1 += l[len(l)//2]
        else:
            # topsort
            good = []
            Q = deque([])
            D = {x: len(B[x] & set(l)) for x in l}
            for v in l:
                if D[v] == 0:
                    Q.append(v)
            while Q:
                x = Q.popleft()
                good.append(x)
                for y in A[x]:
                    if y in D:
                        D[y] -= 1
                        if D[y] == 0:
                            Q.append(y)
            res2 += good[len(good)//2]


    return res1, res2

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    i_sol = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


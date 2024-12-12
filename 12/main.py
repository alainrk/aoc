from utils import *

#########################################################
#########################################################
def solve(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res1, res2 = 0, 0

    G = []
    for i, line in enumerate(lines):
        G.append(list(line))

    R, C = len(G), len(G[0])
    V = set()
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    for r in range(R):
        for c in range(C):
            if (r,c) in V:
                continue

            q = deque([(r,c)])
            A = 0
            P = 0
            PP = {}

            while q:
                r2,c2 = q.popleft()
                if (r2,c2) in V:
                    continue

                V.add((r2,c2))
                A += 1

                for dr,dc in dirs:
                    rr = r2+dr
                    cc = c2+dc

                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r2][c2]:
                        q.append((rr,cc))
                    else:
                        P += 1
                        if (dr,dc) not in PP:
                            PP[(dr,dc)] = set()
                        PP[(dr,dc)].add((r2,c2))

            S = 0
            for _, vs in PP.items():
                VP = set()
                for (pr,pc) in vs:
                    if (pr,pc) not in VP:
                        q = deque([(pr,pc)])
                        S += 1
                        while q:
                            r2,c2 = q.popleft()
                            if (r2,c2) in VP:
                                continue
                            VP.add((r2,c2))
                            for dr,dc in dirs:
                                rr,cc = r2+dr,c2+dc
                                if (rr,cc) in vs:
                                    q.append((rr,cc))
            res1 += A*P
            res2 += A*S

    return res1, res2
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol = solve(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol = }\033[0m")


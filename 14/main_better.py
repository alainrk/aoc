from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    R = 103
    C = 101

    res = 0
    P = []
    for i, line in enumerate(lines):
        # invert x/y for simplicity
        py,px,vy,vx = ints(line)
        P.append((px,py,vx,vy))

    Q = [0, 0, 0, 0]

    # returns quadrant based on x,y
    def p2q(x, y):
       if x < R//2 and y < C//2:
           return 0
       if x >= R//2 and y < C//2:
           return 1
       if x < R//2 and y >= C//2:
           return 2
       if x >= R//2 and y >= C//2:
           return 3

    def printRobots(t, pos):
        print("-" * 100)
        print(f"t={t}")
        for r in range(R):
            for c in range(C):
                if (r,c) in pos:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    # connected comp
    def cc(pos):
        count = 0
        V = set()
        for x,y in pos:
            if (x, y) in V:
                continue
            count += 1
            q = deque([(x,y)])
            while len(q):
                px, py = q.popleft() 
                V.add((px,py))
                for dx, dy in dirs:
                    npx, npy = px + dx, py + dy
                    if npx < 0 or npx >= R or npy < 0 or npy >= C:
                        continue
                    if (npx, npy) not in pos:
                        continue
                    if (npx, npy) in V:
                        continue
                    q.append((npx, npy))
        return count

    possible = 0
    count = 100 if pt == 1 else 8000
    for t in range(count):
        pos = set()
        for i, (px,py,vx,vy) in enumerate(P):
            npx = (px + vx) % R
            npy = (py + vy) % C
            P[i] = (npx, npy, vx, vy)
            pos.add((npx, npy))
        if pt == 2:
            conncomp = cc(pos)
            if conncomp < 300:
                possible += 1
                printRobots(t, pos)

    for i, (px,py,vx,vy) in enumerate(P):
        if px == R//2 or py == C//2:
            continue
        q = p2q(px, py)
        Q[q] += 1

    res = math.prod(Q)

    return res, possible
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    G = [] # graph
    S = [] # trailheads
    for i, line in enumerate(lines):
        l = list(map(int, line))
        G.append(l)
        for i, x in enumerate(l):
            if x == 0:
                S.append((len(G)-1, i))

    R,C = len(G), len(G[0])
    dir = [(-1,0),(0,1),(1,0),(0,-1)]

    for x, y in S:
        V = set()
        # BFS
        Q = deque()
        Q.append((x,y))
        while len(Q) > 0:
            i,j = Q.popleft()
            if pt==1 and (i,j) in V:
                continue
            V.add((i,j))

            if G[i][j] == 9:
                res += 1
                continue

            for dx, dy in dir:
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and (nx,ny) not in V and G[nx][ny]-1 == G[i][j]:
                    Q.append((nx,ny))


    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    RR, CC = -1, -1
    O = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(list(line)):
            if c == '#':
                O.add((i, j))
            if c == '^':
                RR, CC = i, j

    # 0 up, 1 right, 2 down, 3 left => dir = (dir + 1) % 4 to rotate 90'
    dir = 0
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    R,C = len(lines), len(lines[0])
    res = 0

    for i in range(R):
        for j in range(C):
            if i == RR and j == CC:
                continue
            if (i, j) in O:
                continue

            if pt == 2:
                O.add((i, j))
            V = set()
            c = 0
            dir = 0
            rr, cc = RR, CC
            # print(f"{i=}, {j=}, {res=}")

            while True:
                V.add((rr, cc))
                c += 1
                if c > 100000:
                    res += 1
                    break

                while True:
                    bbreak = False
                    nextpos = (rr + move[dir][0], cc + move[dir][1])

                    # outside, return
                    if nextpos[0] >= R or nextpos[0] < 0 or nextpos[1] >= C or nextpos[1] < 0:
                        if pt == 1:
                            return len(V)
                        bbreak = True
                    # obstacle, try next direction
                    if nextpos in O:
                        dir = (dir+1) % 4
                        continue
                    # valid, go ahead
                    if nextpos not in O:
                        rr, cc = nextpos
                        break

                if bbreak:
                    break

            O.remove((i, j))

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = "input.txt"
    sol1 = solve(input_file, 1)
    sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {sol1 = }\033[0m")
    print(f"\033[1m\033[92m[SOLUTION] {sol2 = }\033[0m")


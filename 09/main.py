from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    fs = []
    id = 0
    L = -1 # first empty pos
    # [pos, size][]
    F = [] # free spaces
    FL = -1
    # [pos, size, id][]
    B = []

    for j, c in enumerate(list(lines[0])):
        if j % 2 == 1:
            # set first empty pos
            if L == -1:
                L = len(fs)
            F.append([len(fs), int(c)])
            fs.extend([None] * int(c))
            if FL == -1:
                FL = 0
        else:
            B.append([len(fs), int(c), id])
            fs.extend([id] * int(c))
            id += 1

    N = len(fs)

    if pt == 1:
        for j, c in enumerate(reversed(fs)):
            idx = N - 1 - j # original idx

            if L >= idx or L >= N:
                break

            if c is None:
                continue

            # pt1
            fs[L] = c
            fs[idx] = None

            while True:
                L += 1
                if L >= N or fs[L] is None:
                    break
    else:
        # starting from last of B (blocks)
        # find the first free with the right size for the block
        # if not found B--
        # if found, update fs single chars with the B.index for the B.size
        # keep going backword until next None (B.pos - 1)
        for (bpos, bsize, id) in reversed(B):
            for i,(spos, ssize) in enumerate(F):
                if spos < bpos and bsize <= ssize:
                    for j in range(bsize):
                        assert fs[bpos+j] == id, f'{fs[bpos+j]=}'
                        fs[bpos+j] = None
                        fs[spos+j] = id
                    F[i] = (spos + bsize, ssize-bsize)
                    break

    # checksum
    for j, c in enumerate(fs):
        if c is None: continue
        res += j*c

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION 1] {i_sol = }\033[0m")
    i_sol = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION 2] {i_sol = }\033[0m")


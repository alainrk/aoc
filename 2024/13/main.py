from utils import *

#########################################################
#########################################################
def get_closest(bx, by, rx, ry):
    # Calculate maximum possible steps in x and y direction
    # Using integer division (//) to ensure we don't exceed target
    steps_x = rx // bx if bx != 0 else 0
    steps_y = ry // by if by != 0 else 0
    
    # Take the minimum number of steps that satisfies both x and y constraints
    steps = min(steps_x, steps_y) if (bx != 0 and by != 0) else max(steps_x, steps_y)
    
    # Calculate final position
    final_x = bx * steps
    final_y = by * steps
    
    return final_x, final_y


def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    Ac = 3
    Bc = 1
    res = 0
    c = -1
    M = []
    for i, line in enumerate(lines):
        c = (c+1) % 4
        if c == 0:
            M.append([ ints(line)])
        if c == 1:
            M[len(M)-1].append(ints(line))
        if c == 2:
            M[len(M)-1].append(ints(line))
        if c == 3:
            continue

    for i, m in enumerate(M):
        ax, ay = m[0]
        bx, by = m[1]
        rx, ry = m[2]
        if pt == 2:
            rx += 10000000000000
            ry += 10000000000000

        if pt == 1:
            bbreak = False
            for a in range(101):
                for b in range(101):
                    if (ax*a + bx*b) == rx and (ay*a + by*b) == ry:
                        res += (Ac * a) + (Bc * b)
                        bbreak = True
                        break
                if bbreak:
                    break
        else:
            ca = (rx * by - ry * bx) / (ax * by - ay * bx)
            cb = (rx - ax * ca) / bx
            if ca % 1 == cb % 1 == 0 :
                res += int (ca * 3 + cb)

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


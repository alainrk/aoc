from typing import final
from utils import *
from collections import deque


# BFS in XOR space
def search(target, numbers):
    if target == 0:
        return 0, []

    visited = set()
    q = deque([(0, [])])  # curr value, path

    while q:
        curr, path = q.popleft()
        for n in numbers:
            nv = curr ^ n
            if nv == target:
                return len(path) + 1, path + [n]
            if nv not in visited:
                visited.add(nv)
                q.append((nv, path + [n]))
    return -1, []


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    for i, line in enumerate(lines):
        chunks = line.split(" ")

        finalstate = 0
        for i, c in enumerate(chunks[:1][0].strip("[]")):
            c = 1 if c == "#" else 0
            finalstate += c * pow(2, i)

        # state = [0 for x in finalstate]
        state = 0

        bs = list(map(ints, chunks[1 : len(chunks) - 1]))
        buttons = []
        for b in bs:
            s = 0
            for bb in b:
                s += 1 << bb
            buttons.append(s)

        joltage = chunks[-1]

        res += search(finalstate, buttons)[0]

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    # i_sol2 = solve(input_file, 2)
    # print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

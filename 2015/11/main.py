from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    psw = ""
    for i, line in enumerate(lines):
        psw = line 
        break

    def increment(p):
        curr = len(p) - 1
        while curr >= 0:
            code = ord(p[curr])
            if code == 122:
                p = p[:curr] + "a" + p[curr+1:]
                curr -= 1
            else:
                p = p[:curr] + chr(code + 1) + p[curr+1:]
                # stop
                curr = -1
        return p

    def isValid(psw):
        doubles = 0
        prev, prevJustFound = None, True
        q = deque()
        straight = 0

        for i, c in enumerate(psw):
            if c == prev and not prevJustFound:
                doubles += 1
                prevJustFound = True
            else:
                prevJustFound = False

            q.append(ord(c))
            if len(q) == 4:
               q.popleft()
            if len(q) == 3 and q[0] == q[1] - 1 == q[2] - 2:
                print(q)
                straight += 1
            prev = c
        return doubles == 2 and straight > 0

    while not isValid(psw):
        psw = increment(psw)
    
    return psw

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


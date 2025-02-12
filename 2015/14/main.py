from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    # if pt==2:return

    res = 0
    BATTERY, RESTED, DIST, SCORE = 0, 1, 2, 3
    deers = []
    state = {}
    for i, line in enumerate(lines):
        r = parse("{who} can fly {speed}km/s for {sec} seconds, but then must rest for {rest} seconds.", line)
        deers.append([r["who"], int(r["speed"]), int(r["sec"]), int(r["rest"])])
        state[r["who"]] = [int(r["sec"]), 0, 0, 0]


    SEC = 1000
    SEC = 2503
    for i in range(SEC):
        first, firstKm = [], -1
        for name, speed, flysec, restsec in deers:
            if state[name][BATTERY] == 0 and state[name][RESTED] == restsec:
                state[name][BATTERY] = flysec

            elif state[name][BATTERY] == 0 and state[name][RESTED] < restsec:
                state[name][RESTED] += 1

            # Calc DIST
            if state[name][BATTERY] > 0:
                state[name][RESTED] = 0
                state[name][BATTERY] -= 1
                state[name][DIST] += speed

            # Calc SCORE
            if (state[name][DIST] > firstKm):
                first = [name]
                firstKm = state[name][DIST]
            elif (state[name][DIST] == firstKm):
                first.append(name)

        print(i, state)
        for n in first:
            state[n][SCORE] += 1

    if pt == 1:
        resname = None
        for name, s in state.items():
            if s[DIST] > res:
                resname = name
                res = s[DIST]
        return resname, res

    if pt == 2:
        resname = None
        for name, s in state.items():
            if s[SCORE] > res:
                resname = name
                res = s[SCORE]
        return resname, res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


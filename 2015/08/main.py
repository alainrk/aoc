from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0

    if pt == 1:
        for i, line in enumerate(lines):
            res += len(line) 
            line = line.strip('"')
            line = line.replace('\\\\', '\\')
            line = line.replace('\\"', '\x22')
            # regex match every \xdd
            r = re.findall(r'(\\x([0-9a-f]{2}))', line)
            for code, n in r:
                line = line.replace(code, chr(int(n, 16)))
            res -= len(line)
    else:
        for i, line in enumerate(lines):
            res -= len(line)
            line = line.replace('\"', '--')
            line = line.replace('\\', '--')
            # regex match every \xdd
            res += len(line) + 2


    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

